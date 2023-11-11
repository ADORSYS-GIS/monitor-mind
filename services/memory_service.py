import psutil

def collect_memory_usage():
    memory_usage = psutil.virtual_memory().percent + psutil.swap_memory().percent
    return memory_usage
