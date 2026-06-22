from diffusers import StableDiffusionPipeline
import torch

# Step 1: Prompt
prompt = "A cute orange cat sitting on a chair"

# Step 2: Load model
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16
)
pipe = pipe.to("cuda")

# Step 3: Generate image
image = pipe(prompt).images[0]

# Step 4: Save image
image.save("cat.png")

print("Image generated!")