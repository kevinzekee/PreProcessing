import os
from PIL import Image, ImageEnhance, ImageOps
import random

# Paths
input_folder = r'C:\Users\PC\Desktop\Dataset - BEACON\Dataset - BEACON\Doors'
output_folder = r'C:\Users\PC\Desktop\Dataset - BEACON\PreProcessed'
os.makedirs(output_folder, exist_ok=True)

# Supported image extensions
image_extensions = ('.jpg', '.jpeg', '.png', '.bmp')

# Count existing images in output
existing_files = [f for f in os.listdir(output_folder) if f.lower().endswith(image_extensions)]
existing_files.sort()
existing_count = len(existing_files)

# How many more images are needed
target_total = 1000
images_needed = target_total - existing_count
if images_needed <= 0:
    print(f"✅ You already have {existing_count} images. No need to augment.")
    exit()

print(f"ℹ️ {existing_count} images found. Generating {images_needed} more to reach 500...")

# Load input image files
input_files = [f for f in os.listdir(input_folder) if f.lower().endswith(image_extensions)]
input_files.sort()

# Define augmentation functions
def apply_random_augmentation(image):
    aug_type = random.choice([
        "flip", "rotate", "brightness", "contrast", "invert", "grayscale"
    ])

    if aug_type == "flip":
        return ImageOps.mirror(image)
    elif aug_type == "rotate":
        angle = random.choice([90, 180, 270])
        return image.rotate(angle)
    elif aug_type == "brightness":
        enhancer = ImageEnhance.Brightness(image)
        return enhancer.enhance(random.uniform(0.6, 1.4))
    elif aug_type == "contrast":
        enhancer = ImageEnhance.Contrast(image)
        return enhancer.enhance(random.uniform(0.6, 1.4))
    elif aug_type == "invert":
        return ImageOps.invert(image.convert("RGB"))
    elif aug_type == "grayscale":
        return ImageOps.grayscale(image).convert("RGB")
    else:
        return image

# Augment until we reach 500 total
output_index = existing_count + 1
generated = 0

while generated < images_needed:
    for filename in input_files:
        if generated >= images_needed:
            break

        img_path = os.path.join(input_folder, filename)
        try:
            image = Image.open(img_path).convert("RGB")
        except:
            print(f"❌ Skipped unreadable file: {filename}")
            continue

        image = image.resize((640, 640), Image.Resampling.LANCZOS)
        augmented = apply_random_augmentation(image)

        out_name = f"image{output_index:03d}.jpg"
        out_path = os.path.join(output_folder, out_name)
        augmented.save(out_path)
        print(f"✅ Saved: {out_name}")

        output_index += 1
        generated += 1

print(f"\n🎉 Done! Total images in folder: {existing_count + generated}")
