#!/bin/bash
address="1 Innovation Way, Harrisburg, PA 17110"

lat_delta=0.045
lon_delta=0.055
config_dir_path="./data/config"

# Address to geocode
# address="1600 Amphitheatre Parkway, Mountain View, CA"
echo "Getting lat/long and bounding box for..."
echo "Address: $address"
# URL encode the address
url_address=$(echo "$address" | sed 's/ /%20/g')

# Make the GET request
response=$(curl -s "https://nominatim.openstreetmap.org/search?format=json&q=$url_address")

# Extract the latitude and longitude from the response
lat=$(echo "$response" | jq -r '.[0].lat')
lon=$(echo "$response" | jq -r '.[0].lon')

echo ""
echo "Exact Lat / long:"
echo "Latitude: $lat"
echo "Longitude: $lon"
echo ""

# Approximate a bounding box of 3 miles on all sides of the point
# Note: These values are approximations and will not be perfectly accurate


min_lat=$(echo "$lat - $lat_delta" | bc)
max_lat=$(echo "$lat + $lat_delta" | bc)
min_lon=$(echo "$lon - $lon_delta" | bc)
max_lon=$(echo "$lon + $lon_delta" | bc)

# Print the bounding box
echo "Bounding Box:"
echo "Min Latitude: $min_lat"
echo "Max Latitude: $max_lat"
echo "Min Longitude: $min_lon"
echo "Max Longitude: $max_lon"

echo "Generating config file for bounding box at $config_dir_path..."
# Check if the file exists
if [ -f "$config_dir_path/bbox.json" ]; then
    # Delete the file
    rm "$config_dir_path/bbox.json"
    echo "File $config_dir_path/bbox.json deleted."
else
    echo "File $config_dir_path/bbox.json does not exist."
fi

mkdir -p $config_dir_path
echo "{
  \"min_lat\": \"$min_lat\",
  \"min_long\": \"$min_lon\",
  \"max_lat\": \"$max_lat\",
  \"max_long\": \"$max_lon\",
  \"output_dir\": \"./data/in\"
}" > $config_dir_path/bbox.json
echo "Generated config file for bounding box at $config_dir_path..."