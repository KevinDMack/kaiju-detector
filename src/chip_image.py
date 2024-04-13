from PIL import Image
import os

# Default values for environment variables
DEFAULT_INPUT_DIR = "data/converted"
DEFAULT_OUTPUT_DIR = "data/injected"
DEFAULT_CONFIG = "src/config/config.json"

def chip_image(input_path: str, output_path: str, chip_size: int):
    # Open the image
    img = Image.open(input_path)

    # Get the dimensions of the image
    width, height = img.size

    # Create the output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)

    # Iterate over the image and save each chip
    for i in range(0, width, chip_size):
        for j in range(0, height, chip_size):
            box = (i, j, i+chip_size, j+chip_size)
            chip = img.crop(box)
            chip.save(os.path.join(output_path, f"chip_{i}_{j}.png"))

# Get a list of all PNG files in the directory
png_files = [f for f in os.listdir("./data/converted") if f.endswith('.png')]

def main():
    # Iterate over the PNG files
    for png_file in png_files:
        # Define the input and output paths
        input_path = os.path.join("./data/converted", png_file)
        output_path = os.path.join("./data/chipped", os.path.splitext(png_file)[0])
        training_path = os.path.join("./data/training", os.path.splitext(png_file)[0])

        # Chip the image
        chip_image(input_path, output_path, 100)
        chip_image(input_path, training_path , 100)

if __name__ == "__main__":
    main()