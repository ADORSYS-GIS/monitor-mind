import psutil
import time
import services.time_service as ts

fake_mem = {}
fake_swap = {
    
}
def _collect_ram_usage():
    ram_usage = psutil.virtual_memory().percent
    timestamp = ts.get_history_time()
    return timestamp, ram_usage


def _collect_swap_usage():
    swap_usage = psutil.swap_memory().percent
    timestamp = ts.get_history_time()
    return timestamp, swap_usage


def get_ram_usage_array():
    ram_timestamps, ram_usage = _collect_ram_usage()
    fake_mem[ram_timestamps] = ram_usage
    return [i for i in fake_mem.keys()], [i for i in fake_mem.values()]


def get_swap_usage_array():
    swap_timestamps, swap_usage = _collect_swap_usage()
    fake_swap[swap_timestamps] = swap_usage
    return [i for i in fake_swap.keys()], [i for i in fake_swap.values()]

def calculate_ram_usage():
    """Calculate the current RAM usage as a percentage."""
    timestamp, ram_usage = _collect_ram_usage()
    fake_mem[timestamp] = ram_usage
    
    
def calculate_swap_usage():
    """Calculate the current SWAP usage as a percentage."""
    timestamp, swap_usage = _collect_swap_usage()
    fake_swap[timestamp] = swap_usage
