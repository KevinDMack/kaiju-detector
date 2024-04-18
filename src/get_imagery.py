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

def get_geo_imagery(bbox, output_dir):
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
    os.makedirs("{output_dir}", exist_ok=True)

    # Download the imagery associated with each item
    for item in items:
        # Get the URL of the asset
        print(f"Downloading asset for item {item.id}")
        asset_url = item.assets["image"].href

        # Download the asset and save it to the output directory
        response = requests.get(asset_url)
        with open(f"${output_dir}/{item.id}.tif", "wb") as f:
            f.write(response.content)

        print(f"Downloaded asset for item {item.id}")

    return items

def main():
    try:
        with open('./data/config/bbox.json', 'r') as f:
            bbox_dict = json.load(f)
        
        bbox = [bbox_dict["min_long"], bbox_dict["min_lat"], bbox_dict["max_long"], bbox_dict["max_lat"]]
        output_dir = bbox_dict["output_dir"]
        print(f"output_dir: {output_dir}")
        items = get_geo_imagery(bbox, output_dir)
    except Exception as e:
        print(f"error reading environment variables: {e}")

if __name__ == "__main__":
    main()