import os
import json
import requests
from PIL import Image

# Input and output directories
INPUT_DIR = "./kaiju_data/in"
OUTPUT_DIR = "./kaiju_data/out"
CONFIG_DIR = "./kaiju_data/config"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load configuration from config.json
CONFIG_FILE = "./kaiju_data/config/vision.json"
with open(CONFIG_FILE, "r") as config_file:
    config = json.load(config_file)

ENDPOINT = config["ENDPOINT"]
print(f"Using endpoint: {ENDPOINT}")
PREDICTION_KEY = config["PREDICTION_KEY"]
print(f"Using prediction key: {PREDICTION_KEY}")
PROJECT_ID = config["PROJECT_ID"]
print(f"Using project ID: {PROJECT_ID}")
PUBLISH_ITERATION_NAME = config["PUBLISH_ITERATION_NAME"]
print(f"Using publish iteration name: {PUBLISH_ITERATION_NAME}")

def classify_image(image_path):
    """Submit an image to Custom Vision and return the prediction results."""
    url = f"{ENDPOINT}"
    headers = {
        "Prediction-Key": PREDICTION_KEY,
        "Content-Type": "application/octet-stream"
    }

    with open(image_path, "rb") as image_file:
        response = requests.post(url, headers=headers, data=image_file)
        response.raise_for_status()
        predictions = response.json()

        # Filter predictions with probability > 70%
        filtered_predictions = [
            prediction for prediction in predictions.get("predictions", [])
            if prediction.get("probability", 0) > 0.7
        ]

        return {"predictions": filtered_predictions}

def process_images():
    """Process all images in the input directory and save results."""
    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(INPUT_DIR, filename)
            output_path = os.path.join(OUTPUT_DIR, f"{os.path.splitext(filename)[0]}_result.json")

            print(f"Processing {filename}...")
            try:
                result = classify_image(input_path)
                with open(output_path, "w") as output_file:
                    json.dump(result, output_file, indent=4)
                print(f"Results saved to {output_path}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

if __name__ == "__main__":
    process_images()