# nvidia-smi -L
# nvidia-smi 
# pip install torch torchvision torchaudio diffusers transformers accelerate opencv-python
# photopea.com
# https://unsplash.com/

import torch
from diffusers import I2VGenXLPipeline
from diffusers.utils import load_image, export_to_video

# Load with fp16 variant for efficiency on CUDA
pipe = I2VGenXLPipeline.from_pretrained(
    "ali-vilab/i2vgen-xl", 
    dtype=torch.float16, 
    variant="fp16"
)
# pipe.enable_model_cpu_offload()
pipe.to("cuda")

image = load_image("https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/guitar-man.png").resize((832, 480))
prompt = "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"
generator = torch.Generator("cuda").manual_seed(42)  # For reproducibility
frames = pipe(
    prompt=prompt,
    image=image,
    generator=generator,
    decode_chunk_size=8,
    num_inference_steps=50,  # Optional: improves quality
    guidance_scale=9.0       # Optional: strengthens prompt adherence
).frames[0]
export_to_video(frames, "output/guitar.mp4", fps=7)  # Fixed filename spelling

