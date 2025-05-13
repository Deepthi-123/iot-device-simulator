## iot-device-simulator

### IoT Device Simulator
A Docker-based simulator for generating system metrics and publishing them to an MQTT broker.

* 📦 Python code is packaged as a pip-installable module and included in each container.

* 🐳 Containers are deployed using Docker Compose.

* ⚙️ Use generate-containers.sh to spin up multiple instances of the simulator.
----------------
### Development Environment
This project is developed inside a Dev Container using [Visual Studio Code Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers):

* 📂 The .devcontainer folder defines the containerized development environment.

* 🐍 The container comes pre-installed with Python, pip, and tools like podman and docker-cli for local container testing.

* 📦 The simulator package is mounted into the dev container and editable during development.

* 🧪 Use the terminal inside VS Code to build, test, and publish metrics from the dev environment.

-----------------
### TODO

* 🚀 Create Systemd Service

* 📦 Package as .deb pkg for easier installation

* 🌐 Publish to Local MQTT Broker

* 🧪 Add Tests

* 🔐 Use self signed certificates for communication to the local broker