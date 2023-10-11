#!/bin/bash

# Build the Docker image
docker build -t social-media-assignment .

# Run the Docker container, mapping port 5000 in the container to your host machine
# docker run -p 5050:5050 social-media-assignment

# Run the Docker Compose file
docker-compose up

