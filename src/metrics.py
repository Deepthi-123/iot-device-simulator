import random
import psutil
from datetime import datetime, timezone

def generate_cpu_metrics():
    """
    Generates CPU metrics including CPU usage, temperature, and frequency.
    """
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_temp = round(random.uniform(30.0, 100.0))  # Simulated temperature
    cpu_freq = psutil.cpu_freq().current if psutil.cpu_freq() else None

    return {
        "cpu_usage": cpu_usage,
        "cpu_temp": cpu_temp,
        "cpu_freq": cpu_freq,
        "timestamp": datetime.now(timezone.utc)
    } 

def generate_memory_metrics():
    """
    Generates memory metrics including total, available, and used memory.
    """
    memory = psutil.virtual_memory()
    total_memory = memory.total / (1024 ** 3)  # Convert to GB
    available_memory = memory.available / (1024 ** 3)  # Convert to GB
    used_memory = memory.used / (1024 ** 3)  # Convert to GB

    return {
        "total_memory": total_memory,
        "available_memory": available_memory,
        "used_memory": used_memory,
        "timestamp": datetime.now(timezone.utc)
    }

def generate_disk_metrics():
    """
    Generates disk metrics including total, used, and free disk space.
    """
    disk_usage = psutil.disk_usage('/')
    total_disk = disk_usage.total / (1024 ** 3)  # Convert to GB
    used_disk = disk_usage.used / (1024 ** 3)  # Convert to GB
    free_disk = disk_usage.free / (1024 ** 3)  # Convert to GB

    return {
        "total_disk": total_disk,
        "used_disk": used_disk,
        "free_disk": free_disk,
        "timestamp": datetime.now(timezone.utc)
    }
