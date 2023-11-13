import time
import psutil
import time_service as ts

fake_mem = {}


def _collect_cpu_usage(cpu_threshold = 50):
    cpu_usage = psutil.cpu_percent(interval=1)
    timestamp = ts.get_history_time()
    if cpu_usage > cpu_threshold:
        print(" ")
        print("CPU usage is above threshold", cpu_threshold, "and it's value is: {}%".format(cpu_usage))
        print("Please take necessary measures to make your system function accurately...")
        print("*************************************************************************")
    else:
        print(" ")
        print("CPU usage is stable and it's percentage is: {}%".format(cpu_usage))
        print("*************************************************************************")

    return timestamp, cpu_usage


def get_cpu_usage_array():
    return [i for i in fake_mem.keys()], [i for i in fake_mem.values()]


def calculate_cpu_usage():
    """Calculate the current CPU usage as a percentage."""
    timestamp, cpu_usage = _collect_cpu_usage()
    fake_mem[timestamp] = cpu_usage
    return timestamp, cpu_usage