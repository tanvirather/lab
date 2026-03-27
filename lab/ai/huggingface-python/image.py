# pip install torch transformers diffusers transformers accelerate --break-system-packages

import torch
from diffusers import StableDiffusionPipeline

# 1. Load using float32 (required for standard CPU support)
# 2. Removed .to("cuda") so it defaults to CPU
pipeline = StableDiffusionPipeline.from_pretrained(
    "dreamlike-art/dreamlike-photoreal-2.0", 
    dtype=torch.float16,
    use_safetensors=True,
    local_files_only=True
).to("cuda")

prompt = "an astronaut"
for i in range(1):
    # This will be significantly slower on CPU than on a GPU
    image = pipeline(prompt).images[0]
    image.save(f"output/image-{i}.png")