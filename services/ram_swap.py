import psutil

def collect_swap_ram_usage():
    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    ram_usage = mem.percent
    swap_usage = swap.percent
    return ram_usage, swap_usage