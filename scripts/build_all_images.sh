#!/bin/bash

echo "Building all images..."

echo "Building base image..."
docker build -t kaiju/service-base-kaiju:latest -f ./Dockerfiles/Dockerfile.base .
echo "Built base images..."

echo "Building service images..."

echo "Building service-get-bounding-box image..."
docker build --build-arg SERVICE_NAME=service-get-bounding-box -t kaiju/service-get-bounding-box:latest -f ./Dockerfiles/Dockerfile.service .
echo "Built service-get-bounding-box image..."

echo "Building service-get-satellite-imagery image..."
docker build --build-arg SERVICE_NAME=service-get-satellite-imagery -t kaiju/service-get-satellite-imagery:latest -f ./Dockerfiles/Dockerfile.service .
echo "Built service-get-satellite-imagery image..."

echo "Building service-convert-images image..."
docker build --build-arg SERVICE_NAME=service-convert-images -t kaiju/service-convert-images:latest -f ./Dockerfiles/Dockerfile.service .
echo "Built service-convert-images image..."

echo "Building service-resize-images image..."
docker build --build-arg SERVICE_NAME=service-resize-images -t kaiju/service-resize-images:latest -f ./Dockerfiles/Dockerfile.service .
echo "Built service-resize-images image..."

echo "Building service-inject-kaiju image..."
docker build --build-arg SERVICE_NAME=service-inject-kaiju -t kaiju/service-inject-kaiju:latest -f ./Dockerfiles/Dockerfile.service .
echo "Built service-inject-kaiju image..."

echo "Building service-chip-imagess image..."
docker build --build-arg SERVICE_NAME=service-chip-images -t kaiju/service-chip-images:latest -f ./Dockerfiles/Dockerfile.service .
echo "Built service-chip-images image..."

echo "Built service images..."

echo "All Images built successfully!"