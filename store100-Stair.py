import os
import shutil

# === CONFIGURATION ===
source_folder = r"C:\Users\PC\Desktop\Pre-Processed-Stairs-Test"       # CHANGE THIS
destination_folder = r"C:\Users\PC\Desktop\Stairs100"          # CHANGE THIS
prefix = "stairs"
max_images = 100

# === SETUP ===
os.makedirs(destination_folder, exist_ok=True)

# === GET IMAGE FILES ===
image_extensions = ('.jpg', '.jpeg', '.png')
image_files = sorted(
    [f for f in os.listdir(source_folder) if f.lower().endswith(image_extensions)]
)[:max_images]

# === COPY AND RENAME ===
for idx, filename in enumerate(image_files, start=1):
    src_path = os.path.join(source_folder, filename)
    dst_filename = f"{prefix}{idx:02d}.jpg"
    dst_path = os.path.join(destination_folder, dst_filename)
    shutil.copy2(src_path, dst_path)
    print(f"[✅] {filename} → {dst_filename}")

print(f"\n✔️ Copied {len(image_files)} images to {destination_folder}")
