import os

# Set the directory containing your images
folder_path = r'C:\Users\PC\Desktop\Dataset - BEACON\All'  # Change to your target folder path

# Supported image extensions
image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')

# Get list of image files
files = [f for f in os.listdir(folder_path) if f.lower().endswith(image_extensions)]
files.sort()  # Optional: sort alphabetically

# Rename each image
for index, filename in enumerate(files, start=1):
    ext = os.path.splitext(filename)[1]  # Get file extension
    new_name = f"image{index:02d}{ext}"  # Format as image01.jpg, image02.png, etc.

    src = os.path.join(folder_path, filename)
    dst = os.path.join(folder_path, new_name)

    os.rename(src, dst)
    print(f"Renamed: {filename} -> {new_name}")

print("Renaming complete.")
