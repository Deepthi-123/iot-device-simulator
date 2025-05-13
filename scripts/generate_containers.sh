#!/bin/bash

# Generate simulators from docker image

DEVICE_TYPE="$1"
DEVICE_ID="$2"
SCALE_SIZE="$3"

CONTAINER_ENGINE=

# When the development environment is not VS Code devcontainer
if command -v docker >/dev/null 2>&1; then
    CONTAINER_ENGINE="docker"
elif command -v podman >/dev/null 2>&1; then
    CONTAINER_ENGINE="podman"
fi

"$CONTAINER_ENGINE"-compose up --scale "$SCALE_SIZEß" 