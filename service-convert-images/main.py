import os
from PIL import Image

# Define input and output directories
INPUT_DIR = "kaiju_data/in"
OUTPUT_DIR = "kaiju_data/out"

# Ensure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Iterate through all .tif files in the input directory
for file in os.listdir(INPUT_DIR):
    if file.endswith(".tif"):
        input_path = os.path.join(INPUT_DIR, file)
        base_name = os.path.splitext(file)[0]
        output_path = os.path.join(OUTPUT_DIR, f"{base_name}.png")

        # Open the .tif file and convert it to .png
        with Image.open(input_path) as img:
            img = img.convert("RGBA")  # Ensure the image has an alpha channel
            img.save(output_path, "PNG")

        print(f"Converted {file} to {output_path}")