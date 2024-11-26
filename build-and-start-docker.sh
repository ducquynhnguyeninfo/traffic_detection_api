#!/bin/bash

# Define variables
IMAGE_NAME="du-api"
REPO_NAME="bu8poc"
TAG_NAME="v1.0"

# Build the Docker image
docker build -t ${REPO_NAME}/${IMAGE_NAME}:${TAG_NAME} .

# Push the Docker image to the repository
#docker push ${REPO_NAME}/${IMAGE_NAME}:${TAG_NAME}

docker run -p 8080:80 ${REPO_NAME}/${IMAGE_NAME}:${TAG_NAME}