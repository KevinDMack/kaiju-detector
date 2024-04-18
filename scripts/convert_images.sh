#!/bin/bash

INPUT_DIR="$1"
OUTPUT_DIR="$2"

for file in $INPUT_DIR/*.tif; do
    filename=$(basename "$file")
    base="${filename%.*}"
    gdal_translate -of PNG -a_nodata 0 -scale 0 255 0 255 "$file" "$OUTPUT_DIR/$base.png"
done