#!/bin/bash

INPUT_DIR="$1"
OUTPUT_DIR="$2"

mkdir -p $OUTPUT_DIR

for file in $INPUT_DIR/*.png; do
    filename=$(basename "$file")
    base="${filename%.*}"
    convert "$file" -crop 500x500 \
        -set filename:tile "%[fx:page.x/500]_%[fx:page.y/500]_${base}" \
        +repage +adjoin "$OUTPUT_DIR/%[filename:tile].png"
done