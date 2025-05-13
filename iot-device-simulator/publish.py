import time
import random
import asyncio
import logging
from paho.mqtt import client as mqtt_client
from metrics import generate_cpu_metrics, generate_memory_metrics, generate_disk_metrics

logger = logging.getLogger(__name__)

# Configuration for MQTT Broker
BROKER = "mqtt.eclipse.org"  # Use a public broker for simplicity, or your own broker
PORT = 1883
TOPIC = "iot-sim/publish/mock-data"

#   Convert synchronous functions to async
async def generate_async(callback):
    await asyncio.sleep(random.uniform(1, 3))
    return callback()

# Publish sensor data async
async def publish_sensor_data(client):
    while True:
        metrics = await asyncio.gather(
            generate_async(generate_cpu_metrics),
            generate_async(generate_memory_metrics),
            generate_async(generate_disk_metrics)
        )
        combined = {k: v for metric in metrics for k, v in metric.items()}
        publish_data(client, combined)
        await asyncio.sleep(5)

# Publish payload
def publish_data(client, sensor_data):
    payload = str(sensor_data)  # Convert the dict to a string
    result = client.publish(TOPIC, payload, qos=1)
    if result.rc == mqtt_client.MQTT_ERR_SUCCESS:
        logger.info(f"Published data: {payload}")
    else:
        logger.info(f"Failed to publish message: {result.rc}")    


async def run_metrics_loop(client_id):
    # Create an MQTT client instance
    client = mqtt_client.Client(client_id)
    
    # Connect to the MQTT broker
    client.connect(BROKER, PORT)
    
    # Start client loop
    client.loop_start()

    # Start publishing data
    await publish_sensor_data(client)
