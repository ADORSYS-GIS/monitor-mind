import psutil
import os
import datetime
import time

def get_home_directory():
    """Get the home directory of the user."""
    return os.path.expanduser("~")

def create_log_file():
# Create the log file in the home directory if it doesn't exist.
    log_file_path = os.path.join(get_home_directory(), "ram_swap_usage.log")
    if not os.path.exists(log_file_path):
        with open(log_file_path, "w") as file:
            file.write("Timestamp, RAM Usage (%), Swap Usage (%)\n")
    return log_file_path

log_file_path = create_log_file()

def collect_swap_ram_usage():
    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    ram_usage = mem.percent
    swap_usage = swap.percent
    return ram_usage, swap_usage

def start_collection():
    while True:
        ram_usage, swap_usage = collect_swap_ram_usage()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp}, {ram_usage}, {swap_usage}\n"
        with open(log_file_path, "a") as file:
            file.write(log_entry)
            file.flush()
        time.sleep(1)  # Adjust the sleep duration as per your requirements