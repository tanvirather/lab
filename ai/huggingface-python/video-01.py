# nvidia-smi -L
# nvidia-smi 
# pip install torch torchvision torchaudio diffusers transformers accelerate opencv-python
# photopea.com
# https://unsplash.com/


import torch
from diffusers import StableVideoDiffusionPipeline
from diffusers.utils import load_image, export_to_video

# Load with fp16 variant for efficiency on CUDA
pipe = StableVideoDiffusionPipeline.from_pretrained(
    "stabilityai/stable-video-diffusion-img2vid-xt", 
    torch_dtype=torch.float16, 
    variant="fp16"
)
# pipe.enable_model_cpu_offload()
pipe.to("cuda")

prompt = "A man with short gray hair plays a red electric guitar."
image = load_image("https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/guitar-man.png")
image = image.resize((1024, 576))  # Required input resolution [web:2]

generator = torch.Generator("cuda").manual_seed(42)  # For reproducibility
frames = pipe(
    image=image, 
    decode_chunk_size=8,  # Reduces VRAM usage
    generator=generator
).frames[0]

export_to_video(frames, "output/guitar.mp4", fps=7)  # Fixed filename spelling

