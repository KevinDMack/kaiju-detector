import json
import logging
import os
import sys
import random 
import time
import shutil 

from PIL import Image 
from typing import Union
from pathlib import Path

import os
import requests
import pystac_client
import rasterio
import matplotlib.pyplot as plt

from datetime import datetime, timedelta

# Default values for environment variables
DEFAULT_INPUT_DIR = "data/converted"
DEFAULT_OUTPUT_DIR = "data/injected"
DEFAULT_CONFIG = "src/config/config.json"


def convert_geotiffs_to_png(input_path: str, output_path: str):
    # Get a list of all GeoTIFF files in the input directory
    geotiff_files = [f for f in os.listdir(input_path) if f.endswith('.tif')]

    # Iterate over the GeoTIFF files
    for geotiff_file in geotiff_files:
        # Open the GeoTIFF file
        print("Opening {geotiff_file}")
        with rasterio.open(os.path.join(input_path, geotiff_file)) as src:
            img = src.read()

        # Plot the image
        print("Plotting the image")
        plt.imshow(img[0])
        plt.axis('off')

        # Save the image as a PNG
        print("Saving the image as a PNG")
        png_file = os.path.splitext(geotiff_file)[0] + '.png'
        plt.savefig(os.path.join(output_path, png_file), bbox_inches='tight', pad_inches=0)

        print(f"Converted {geotiff_file} to {png_file}")

        print(f"Removing {geotiff_file}")
        os.remove(os.path.join(input_path, geotiff_file))
        print(f"Removed {geotiff_file}")

def main():
    try:
        convert_geotiffs_to_png("./data/in", "./data/converted")
    except Exception as e:
        print(f"error reading environment variables: {e}")

if __name__ == "__main__":
    main()