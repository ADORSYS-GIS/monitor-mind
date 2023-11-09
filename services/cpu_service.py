import time

import psutil

fake_mem = {}


def _collect_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    timestamp = time.time()
    return int(timestamp * 1000), cpu_usage


def get_cpu_usage_array():
    return [i for i in fake_mem.keys()], [i for i in fake_mem.values()]


def calculate_cpu_usage():
    """Calculate the current CPU usage as a percentage."""
    timestamp, cpu_usage = _collect_cpu_usage()
    fake_mem[timestamp] = cpu_usage
