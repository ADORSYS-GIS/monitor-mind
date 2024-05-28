import psutil
import services.time_service as ts

def get_memory_usage(mem_threshold = 60):
    """Get the current memory RAM usage as a percentage."""
    mem_usages = psutil.virtual_memory().used
    mem_total = psutil.virtual_memory().total
    mem_percentage = (mem_usages / mem_total) * 100
    timestamp = ts.get_history_time()
    if mem_percentage > mem_threshold:
        print(" ")
        print("Memory usage is above threshold", (str(mem_threshold)+'%'), "and it's value is: {}%".format(round(mem_percentage, 2)))
        print("Please take necessary measures to make your system function accurately...")
        print("*************************************************************************")
    else:
        print(" ")
        print("The memory usage is stable and it's value is: {}%".format(round(mem_percentage, 2)))
    return timestamp, mem_percentage

