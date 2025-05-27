import os
from PIL import Image

# Directories for input and output
input_dir = "kaiju_data/in"
output_dir = "kaiju_data/out"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Loop through each PNG file in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".png"):
        file_path = os.path.join(input_dir, filename)
        print(f"Processing {file_path}...")

        # Open the image
        with Image.open(file_path) as img:
            width, height = img.size
            tile_size = 500

            # Crop the image into 500x500 tiles
            tile_count = 0
            for top in range(0, height, tile_size):
                for left in range(0, width, tile_size):
                    # Define the box for cropping
                    box = (left, top, min(left + tile_size, width), min(top + tile_size, height))
                    tile = img.crop(box)

                    # Save the tile
                    tile_filename = f"{os.path.splitext(filename)[0]}_tile_{tile_count}.png"
                    tile.save(os.path.join(output_dir, tile_filename))
                    tile_count += 1