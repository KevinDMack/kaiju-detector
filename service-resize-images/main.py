import os
from PIL import Image

INPUT_DIR = "kaiju_data/in"
OUTPUT_DIR = "kaiju_data/out"

# Ensure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Iterate over all PNG files in the input directory
for file_name in os.listdir(INPUT_DIR):
    if file_name.endswith(".png"):
        input_path = os.path.join(INPUT_DIR, file_name)
        output_path = os.path.join(OUTPUT_DIR, file_name)

        # Open the image
        with Image.open(input_path) as img:
            # Calculate new dimensions
            new_width = img.width // 10
            new_height = img.height // 10

            # Resize the image
            resized_img = img.resize((new_width, new_height))

            # Save the resized image to the output directory
            resized_img.save(output_path)