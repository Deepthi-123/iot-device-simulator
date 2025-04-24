FROM debian:bookworm-slim

#Update & upgrade
RUN apt-get update && apt-get upgrade -y

RUN apt install python3 -y && \
    apt install python3-pip -y && \
    # to avoid force use of venv as there will be no need to maintain multiple versions of python
    python3 -m pip config set global.break-system-packages true && \
    mkdir -p scripts/

COPY scripts/* scripts/

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# # Run the app
# CMD ["python", "app.py"]
