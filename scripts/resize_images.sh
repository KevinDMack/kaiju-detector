#!/bin/bash

INPUT_DIR="$1"
OUTPUT_DIR="$2"

for file in $INPUT_DIR/*.png; do
    filename=$(basename "$file")
    width=$(identify -format "%w" "$file")
    height=$(identify -format "%h" "$file")
    new_width=$((width / 10))
    new_height=$((height / 10))
    convert "$file" -resize ${new_width}x${new_height}! "$OUTPUT_DIR/$filename"
done