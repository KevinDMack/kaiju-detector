#!/bin/bash

# Use the argument passed in $1 to overwrite the default LOCAL_REGISTRY
LOCAL_REGISTRY=${1:-localhost:5000}

echo "Using local registry: $LOCAL_REGISTRY"

echo "Building all images..."

echo "Building base image..."
docker build -t kaiju/service-base-kaiju:latest -f ./Dockerfiles/Dockerfile.base .
docker tag kaiju/service-base-kaiju:latest $LOCAL_REGISTRY/kaiju/service-base-kaiju:latest
docker push $LOCAL_REGISTRY/kaiju/service-base-kaiju:latest
echo "Built and pushed base image..."

echo "Building service images..."

echo "Building service-get-bounding-box image..."
docker build --build-arg SERVICE_NAME=service-get-bounding-box -t kaiju/service-get-bounding-box:latest -f ./Dockerfiles/Dockerfile.service .
docker tag kaiju/service-get-bounding-box:latest $LOCAL_REGISTRY/kaiju/service-get-bounding-box:latest
docker push $LOCAL_REGISTRY/kaiju/service-get-bounding-box:latest
echo "Built and pushed service-get-bounding-box image..."

echo "Building service-get-satellite-imagery image..."
docker build --build-arg SERVICE_NAME=service-get-satellite-imagery -t kaiju/service-get-satellite-imagery:latest -f ./Dockerfiles/Dockerfile.service .
docker tag kaiju/service-get-satellite-imagery:latest $LOCAL_REGISTRY/kaiju/service-get-satellite-imagery:latest
docker push $LOCAL_REGISTRY/kaiju/service-get-satellite-imagery:latest
echo "Built and pushed service-get-satellite-imagery image..."

echo "Building service-convert-images image..."
docker build --build-arg SERVICE_NAME=service-convert-images -t kaiju/service-convert-images:latest -f ./Dockerfiles/Dockerfile.service .
docker tag kaiju/service-convert-images:latest $LOCAL_REGISTRY/kaiju/service-convert-images:latest
docker push $LOCAL_REGISTRY/kaiju/service-convert-images:latest
echo "Built and pushed service-convert-images image..."

echo "Building service-resize-images image..."
docker build --build-arg SERVICE_NAME=service-resize-images -t kaiju/service-resize-images:latest -f ./Dockerfiles/Dockerfile.service .
docker tag kaiju/service-resize-images:latest $LOCAL_REGISTRY/kaiju/service-resize-images:latest
docker push $LOCAL_REGISTRY/kaiju/service-resize-images:latest
echo "Built and pushed service-resize-images image..."

echo "Building service-inject-kaiju image..."
docker build --build-arg SERVICE_NAME=service-inject-kaiju -t kaiju/service-inject-kaiju:latest -f ./Dockerfiles/Dockerfile.service .
docker tag kaiju/service-inject-kaiju:latest $LOCAL_REGISTRY/kaiju/service-inject-kaiju:latest
docker push $LOCAL_REGISTRY/kaiju/service-inject-kaiju:latest
echo "Built and pushed service-inject-kaiju image..."

echo "Building service-chip-images image..."
docker build --build-arg SERVICE_NAME=service-chip-images -t kaiju/service-chip-images:latest -f ./Dockerfiles/Dockerfile.service .
docker tag kaiju/service-chip-images:latest $LOCAL_REGISTRY/kaiju/service-chip-images:latest
docker push $LOCAL_REGISTRY/kaiju/service-chip-images:latest
echo "Built and pushed service-chip-images image..."

echo "Built and pushed all service images successfully!"