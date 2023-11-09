import time

import psutil

fake_mem = {}


def _collect_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1, percpu=True)
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")  # Format the timestamp as desired
    return timestamp, cpu_usage


def get_cpu_usage_array():
    return [i for i in fake_mem.keys()], [i for i in fake_mem.values()]


def calculate_cpu_usage():
    """Calculate the current CPU usage as a percentage."""
    timestamp, cpu_usage = _collect_cpu_usage()
    fake_mem[timestamp] = cpu_usage


cpu_data_history = []
