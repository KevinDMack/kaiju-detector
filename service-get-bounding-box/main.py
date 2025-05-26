import os
import json
import urllib.parse
import urllib.request

# Constants
LAT_DELTA = 0.0289
LON_DELTA = 0.0377
CONFIG_DIR_PATH = "./kaiju_data/config"
ADDRESS_FILE_PATH = os.path.join(CONFIG_DIR_PATH, "address.json")
OUTPUT_FILE_PATH = os.path.join(CONFIG_DIR_PATH, "bbox.json")

def read_address_from_config():
    """Reads the address from the configuration file."""
    if not os.path.exists(ADDRESS_FILE_PATH):
        raise FileNotFoundError(f"Address configuration file not found at {ADDRESS_FILE_PATH}")
    
    with open(ADDRESS_FILE_PATH, "r") as file:
        data = json.load(file)
        return data.get("full_street_address", "").strip()

def get_lat_lon(address):
    """Fetches latitude and longitude for the given address using OpenStreetMap's Nominatim API."""
    url_address = urllib.parse.quote(address)
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={url_address}"
    
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
        if not data:
            raise ValueError(f"No results found for address: {address}")
        return float(data[0]["lat"]), float(data[0]["lon"])

def calculate_bounding_box(lat, lon):
    """Calculates the bounding box based on latitude and longitude."""
    min_lat = lat - LAT_DELTA
    max_lat = lat + LAT_DELTA
    min_lon = lon - LON_DELTA
    max_lon = lon + LON_DELTA
    return min_lat, max_lat, min_lon, max_lon

def write_bounding_box_to_config(min_lat, max_lat, min_lon, max_lon):
    """Writes the bounding box to a JSON configuration file."""
    os.makedirs(CONFIG_DIR_PATH, exist_ok=True)
    
    if os.path.exists(OUTPUT_FILE_PATH):
        os.remove(OUTPUT_FILE_PATH)
        print(f"File {OUTPUT_FILE_PATH} deleted.")
    
    bbox_data = {
        "min_lat": min_lat,
        "min_long": min_lon,
        "max_lat": max_lat,
        "max_long": max_lon,
        "output_dir": "./kaiju_data/in"
    }
    
    with open(OUTPUT_FILE_PATH, "w") as file:
        json.dump(bbox_data, file, indent=4)
    print(f"Generated config file for bounding box at {OUTPUT_FILE_PATH}...")

def main():
    try:
        # Read address from config
        address = read_address_from_config()
        if not address:
            raise ValueError("Address is empty in the configuration file.")
        
        print("Getting lat/long and bounding box for...")
        print(f"Address: {address}")
        
        # Get latitude and longitude
        lat, lon = get_lat_lon(address)
        print("\nExact Lat / long:")
        print(f"Latitude: {lat}")
        print(f"Longitude: {lon}\n")
        
        # Calculate bounding box
        min_lat, max_lat, min_lon, max_lon = calculate_bounding_box(lat, lon)
        print("Bounding Box:")
        print(f"Min Latitude: {min_lat}")
        print(f"Max Latitude: {max_lat}")
        print(f"Min Longitude: {min_lon}")
        print(f"Max Longitude: {max_lon}")
        
        # Write bounding box to config
        write_bounding_box_to_config(min_lat, max_lat, min_lon, max_lon)
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()