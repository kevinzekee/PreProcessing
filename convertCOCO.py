import json
import os

# === CONFIGURATION ===
input_json = r"C:\Users\PC\Desktop\result.json"
output_json = r"C:\Users\PC\Desktop\annotations.json"

# === CONFIGURATION ===
image_dir = r"C:\Users\PC\Desktop\100Test Image"  # Relative directory where images will be stored for training

# === LOAD AND FIX ===
with open(input_json, "r") as f:
    data = json.load(f)

# Fix file names in 'images'
for img in data["images"]:
    full_path = img["file_name"]
    file_name = os.path.basename(full_path)
    img["file_name"] = os.path.join(image_dir, file_name).replace("\\", "/")

# === SAVE ===
with open(output_json, "w") as f:
    json.dump(data, f, indent=2)

print(f"✅ Fixed COCO JSON saved to: {output_json}")
