import psutil
import time
import services.time_service as ts

fake_mem = {}

def _collect_ram_usage():
    mem_usage = psutil.virtual_memory().percent
    timestamp = ts.get_history_time()
    return timestamp, mem_usage

# def _collect_swap_usage():
#     # swap_usage = psutil.swap_memory().percent
#     timestamp = ts.get_history_time()
#     return timestamp, swap_usage

def get_ram_swap_usage_array():
    ram_timestamps, ram_usage = _collect_ram_usage()
    fake_mem[ram_timestamps] = ram_usage
    return [i for i in fake_mem.keys()], [i for i in fake_mem.values()]


def calculate_ram_usage():
    """Calculate the current RAM usage as a percentage."""
    timestamp, ram_usage = _collect_ram_usage()
    fake_mem[timestamp] = ram_usage