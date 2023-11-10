import psutil
import services.time_service as ts

fake_ram_mem = {}
fake_swap_mem = {}

def get_memory_usage():
    """Get the current memory (RAM and Swap) usage as a percentage."""
    ram_usage = psutil.virtual_memory()
    swap_usage = psutil.swap_memory()

    ram_timestamp = ts.get_history_time()
    swap_timestamp = ts.get_history_time()

    return ram_timestamp, ram_usage, swap_timestamp, swap_usage

def get_ram_usage_array():
    timestamps = [i for i in fake_ram_mem.keys()]
    ram_usage = [i for i in fake_ram_mem.values()]
    return timestamps, ram_usage

def calculate_ram_usage():
    timestamp, _, _, ram_usage = get_memory_usage()
    fake_ram_mem[timestamp] = ram_usage

def get_swap_usage_array():
    timestamps = [i for i in fake_swap_mem.keys()]
    swap_usage = [i for i in fake_swap_mem.values()]
    return timestamps, swap_usage

def calculate_swap_usage():
    timestamp, _, _, _, swap_usage = get_memory_usage()
    fake_swap_mem[timestamp] = swap_usage