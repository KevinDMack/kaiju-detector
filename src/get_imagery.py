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
BBOX_CONFIG_PATH = "data/config/bbox.json"

def get_geo_imagery(bbox):
    # Create a STAC client
    stac = pystac_client.Client.open("https://planetarycomputer.microsoft.com/api/stac/v1")

    # Define the collection
    collection_id = "naip"

    # Calculate the date one year ago from today
    one_year_ago = datetime.now() - timedelta(days=730)
    one_year_ago_str = one_year_ago.strftime("%Y-%m-%d")

    # Search for items in the collection within the bounding box from the past year
    print(f"Searching for items in collection {collection_id} within bounding box {bbox}")
    search = stac.search(collections=[collection_id], bbox=bbox, datetime=f"{one_year_ago_str}/{datetime.now().strftime('%Y-%m-%d')}", sortby=["-datetime"])
    print(f"Search returned {search.matched()} items")

    # Get the items
    items = search.item_collection()
    items = list(items)

    # Print the number of items found
    print(f"Found {len(items)} items")

    # Create the output directory if it doesn't exist
    os.makedirs("./data/in", exist_ok=True)

    # Download the imagery associated with each item
    for item in items:
        # Get the URL of the asset
        print(f"Downloading asset for item {item.id}")
        asset_url = item.assets["image"].href

        # Download the asset and save it to the output directory
        response = requests.get(asset_url)
        with open(f"./data/in/{item.id}.tif", "wb") as f:
            f.write(response.content)

        print(f"Downloaded asset for item {item.id}")

    return items

def main():
    input_dir = os.getenv("APP_INPUT_DIR", DEFAULT_INPUT_DIR)
    output_dir = os.getenv("APP_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    config = os.getenv("APP_CONFIG", DEFAULT_CONFIG)

    try:
        with open('./data/config/bbox.json', 'r') as f:
            bbox_dict = json.load(f)
        
        bbox = [bbox_dict["min_long"], bbox_dict["min_lat"], bbox_dict["max_long"], bbox_dict["max_lat"]]
        # bbox = [-76.9321, 40.2426, -76.7936, 40.3363] 
        items = get_geo_imagery(bbox)
    except Exception as e:
        print(f"error reading environment variables: {e}")

if __name__ == "__main__":
    main()