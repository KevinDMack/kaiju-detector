import json
import logging
import os
import sys
import random 
import time
import shutil 
import fnmatch

from PIL import Image 
from typing import Union
from pathlib import Path

import os
import requests
import pystac_client
import rasterio
import matplotlib.pyplot as plt

from datetime import datetime, timedelta

DEFAULT_INPUT_DIR = f"./kaiju_data/in"
DEFAULT_OUTPUT_DIR = f"./kaiju_data/out/"

DEFAULT_CONFIG = "src/config/config.json"

def inject_godzilla(input_path : str, output_path : str, config_path : str):
    print(f"input data directory {input_path}")
    print(f"output data directory {output_path}")
    print(f"config file path {config_path}")

    output_path.mkdir(parents=True, exist_ok=True)

    print(f"Loading Configuration File {config_path}")
    config_file = open(config_path)
    config = json.load(config_file)
    print(f"Loaded Configuration File {config_path}")

    inbox = os.listdir(input_path)
    for img in inbox:
        print(f"Loading tile image {img}")
        img_path = os.path.join(input_path,img)
        save_path = os.path.join(output_path,img)

        print(f"Checking if {img_path} is an image file")
        extensions = ( "jpg","png","bmp","gif" )
        if img_path.endswith(extensions):
            print(f"{img_path} is an image, proceeding with injection")
            tile = Image.open(img_path)
            print(f"Loaded tile image {img}")

            monster_entries = config["monster"]
            monster_list = monster_entries.split(",")

            print(len(monster_list))
            for monster in monster_list:
                print(f"Loading monster file {monster}")
                monster_path = f"./src/images/{monster}.png"
                exists = os.path.exists(monster_path)
                print(f"Monster file {monster} exists = {exists}")
                print(f"Loaded monster file {monster}")
                
                print("Loading monster image")
                monster_image = Image.open(monster_path)
                print("Loaded monster image")

                print("Resizing Monster image")
                current_size = monster_image.size
                print(f"Current size of image {current_size}")
                size_width = int(config["size_width"])
                size_height = int(config["size_height"])
                new_size = (size_width, size_height)
                resized_monster_image = monster_image.resize(new_size)
                resized_monster_image_size = resized_monster_image.size
                print(f"New Current size of image {resized_monster_image_size}")
                print(f"Monster Resized to {resized_monster_image_size}")
                print("Resized Monster image")

                run_random = config["run_random"]
                if (run_random.lower() == "true"):
                    print("Determining placement at random")
                    image_x, image_y = tile.size
                    max_x = image_x - size_width
                    max_y = image_y - size_height   
                    start_x = random.randrange(0,max_x)
                    start_y = random.randrange(0,max_y)
                    print(f"Determined Random Position ({start_x},{start_y})")
                else:
                    print("Retrieving Placement Coordinates")
                    start_x = int(config["start_coordinate_x"])
                    start_y = int(config["start_coordinate_y"])
                    print("Retrieved Placement Coordinates")

                print(f"Overlaying Image with {monster}")
                tile.paste(resized_monster_image, (start_x, start_y), mask=resized_monster_image)
                print(f"Overlay Complete for Image with {monster}")

                print(f"Saving Output Image")
                tile.save(save_path)
                print(f"Saved Output Image")
        else:
            print("File is not an image, copying to destination directory")
            sourcePath = img_path
            destinationPath = save_path
            print(f"Copying file from {sourcePath} to {destinationPath}")
            shutil.copyfile(sourcePath,destinationPath)
            print(f"Copied file from {sourcePath} to {destinationPath}")

    print("Godzilla Injection Complete")

def main():
    input_dir = os.getenv("APP_INPUT_DIR", DEFAULT_INPUT_DIR)
    output_dir = os.getenv("APP_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    config = os.getenv("APP_CONFIG", DEFAULT_CONFIG)

    input_path = Path(input_dir).resolve()
    output_path = Path(output_dir).resolve()
    config_path = Path(config).resolve()

    try:
        inject_godzilla(input_path, output_path, config_path)
    except Exception as e:
        print(f"error reading environment variables: {e}")

if __name__ == "__main__":
    main()