# Run Python

```sh
sudo apt install --yes python3 python3-pip python3-venv

rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
deactivate

pip install torch transformers accelerate huggingface_hub
python3 main.py


python generate_from_file.py \
  --input prompt.txt \
  --outdir ./outputs \
  --model deepseek-ai/deepseek-coder-1.3b-base \
  --cache_dir ./tmp \
  --max_new_tokens 12

```
