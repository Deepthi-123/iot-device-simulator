import os
import asyncio
from publish import run_metrics_loop

if __name__ == "__main__":

    client_id = os.getenv("DEVICE_ID", "DEFAULT_DEVICE_001")
    asyncio.run(run_metrics_loop(client_id))