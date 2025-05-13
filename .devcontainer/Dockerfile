# Use an appropriate base image
FROM debian:bookworm

# Install Podman and necessary dependencies
RUN apt-get update && \
    apt-get install -y \
    git \
    podman \
    sudo \
    curl \
    gnupg2 \
    lsb-release \
    python3 \
    python3-pip \
    && apt-get clean

# Install podman-compose using pip
RUN pip3 install --no-cache-dir podman-compose --break-system-packages

# Set the working directory for the container and root user
WORKDIR /workspace
USER root

# Define the default shell (optional)
SHELL ["/bin/bash", "-c"]
