image_label="kaiju"
echo "Starting image building..."
echo "Running build of base image..."
docker build -t $image_label/kaiju-base:0.0.1 -f ./Dockerfiles/Dockerfile.base .
echo "Ran build of base image...."
echo "Running build of base image..."
docker build -t $image_label/kaiju-get:0.0.1 -f ./Dockerfiles/Dockerfile.get_imagery .
echo "Ran build of base image...."
echo "Running build of image convert image..."
docker build -t $image_label/kaiju-convert:0.0.1 -f ./Dockerfiles/Dockerfile.convert_imagery .
echo "Ran build of convert image...."
echo "Running build of kaiju image injector..."
docker build -t $image_label/kaiju-inject:0.0.1 -f ./Dockerfiles/Dockerfile.inject_kaiju .
echo "Ran Build of kaiju image injector...."
echo "All images created successfully."