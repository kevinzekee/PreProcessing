import base64
import os
import json

# === CONFIGURATION ===
image_folder = r"C:\Users\PC\Desktop\Pre-Processed-Stairs-Test"  # <- change this
output_json = r"C:\Users\PC\Desktop\stairs_tasks.json"

# === FUNCTION ===
def encode_image_to_base64(path):
    with open(path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode("utf-8")
        return f"data:image/jpeg;base64,{encoded}"

# === PROCESS ===
tasks = []
for file in sorted(os.listdir(image_folder)):
    if file.lower().endswith(('.jpg', '.jpeg', '.png')):
        full_path = os.path.join(image_folder, file)
        encoded_image = encode_image_to_base64(full_path)
        tasks.append({
            "image": encoded_image
        })

# === EXPORT ===
with open(output_json, "w", encoding="utf-8") as f:
    json.dump(tasks, f, indent=2)

print(f"✅ Exported {len(tasks)} image tasks to {output_json}")
