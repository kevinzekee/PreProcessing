import os
from PIL import Image, ImageOps
import numpy as np
import shutil

# === CONFIGURATION ===
input_folder = r"C:\Users\PC\Desktop\Staircase Dataset(1)\Staircase Dataset"
output_folder = r"C:\Users\PC\Desktop\Pre-Processed-Stairs-Test"
expected_size = (640, 640)
prefix = "stairs"

# === SETUP ===
os.makedirs(output_folder, exist_ok=True)
image_files = sorted([f for f in os.listdir(input_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])

count = 1

for file in image_files:
    path = os.path.join(input_folder, file)
    try:
        with Image.open(path) as img:
            # Resize if needed
            if img.size != expected_size:
                img = img.resize(expected_size)

            # Convert to RGB just in case
            img = img.convert("RGB")

            # Normalize (for training — we don't save this version)
            normalized = np.array(img) / 255.0  # Float32 in range [0, 1]

            # Save original
            new_name = f"{prefix}{count:02d}.jpg"
            new_path = os.path.join(output_folder, new_name)
            img.save(new_path)
            print(f"[✅] Saved {new_name}")
            count += 1

            # --- Data Augmentation: Flip ---
            flipped = ImageOps.mirror(img)
            flip_name = f"{prefix}{count:02d}.jpg"
            flip_path = os.path.join(output_folder, flip_name)
            flipped.save(flip_path)
            print(f"[🔁] Saved flipped as {flip_name}")
            count += 1

    except Exception as e:
        print(f"[⚠️] Error processing {file}: {e}")

print(f"\n✔️ Finished. Processed images saved in: {output_folder}")
