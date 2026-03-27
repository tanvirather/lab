#!/usr/bin/env python3
import argparse
from pathlib import Path
from datetime import datetime

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


def load_model_and_tokenizer(model_name: str, cache_dir: Path, trust_remote_code: bool = True):
    model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir=cache_dir, trust_remote_code=trust_remote_code)
    tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir, trust_remote_code=trust_remote_code)
    return model, tokenizer

def read_prompt(input_file: Path) -> str:
    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")
    return input_file.read_text(encoding="utf-8")


def generate_text(model, tokenizer, prompt: str, max_new_tokens: int = 128, temperature: float = 0.8, top_p: float = 0.95):
    device = model.device  # model already placed by HF internals
    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            temperature=temperature,
            top_p=top_p,
            eos_token_id=tokenizer.eos_token_id
        )
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return text


def save_output(output_dir: Path, output_text: str, base_name: str = "generation"):
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Save a clean text file and also a "full" file with the prompt included in case the model echoed it.
    out_txt = output_dir / f"{base_name}_{timestamp}.txt"
    out_all = output_dir / f"{base_name}_{timestamp}.all.txt"

    # If the model echoed the prompt, both files will look similar; still useful to keep both variants.
    out_txt.write_text(output_text, encoding="utf-8")
    out_all.write_text(output_text, encoding="utf-8")

    return out_txt, out_all


def main():
    parser = argparse.ArgumentParser(description="Generate text from a prompt file and save output.")
    parser.add_argument("--input", "-i", type=Path, required=True, help="Path to the input prompt file (UTF-8).")
    parser.add_argument("--outdir", "-o", type=Path, required=True, help="Directory to save outputs.")
    parser.add_argument("--model", "-m", type=str, default="deepseek-ai/deepseek-coder-1.3b-base", help="Hugging Face model name.")
    parser.add_argument("--cache_dir", type=Path, default=Path("./tmp"), help="Cache directory for model files.")
    parser.add_argument("--max_new_tokens", type=int, default=128, help="Maximum number of new tokens to generate.")
    parser.add_argument("--temperature", type=float, default=0.8, help="Sampling temperature.")
    parser.add_argument("--top_p", type=float, default=0.95, help="Top-p nucleus sampling.")
    parser.add_argument("--base_name", type=str, default="generation", help="Base filename for outputs.")
    args = parser.parse_args()

    prompt = read_prompt(args.input)
    model, tokenizer = load_model_and_tokenizer(args.model, args.cache_dir)

    # Optionally move to CUDA if available (helps performance)
    if torch.cuda.is_available():
        model = model.to("cuda")

    output_text = generate_text(
        model=model,
        tokenizer=tokenizer,
        prompt=prompt,
        max_new_tokens=args.max_new_tokens,
        temperature=args.temperature,
        top_p=args.top_p
    )

    out_txt, out_all = save_output(args.outdir, output_text, base_name=args.base_name)
    print(f"Saved output:\n - {out_txt}\n - {out_all}")


if __name__ == "__main__":
    main()
