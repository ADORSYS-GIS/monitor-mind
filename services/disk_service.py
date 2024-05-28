import psutil
import services.time_service as ts

def get_disk_usage(disk_threshold = 70):
    """Get the current memory DISK usage as a percentage."""
    disk_usages = psutil.disk_usage('/').used
    disk_total = psutil.disk_usage('/').total
    disk_percentage = (disk_usages / disk_total) * 100
    timestamp = ts.get_history_time()
    if disk_percentage > disk_threshold:
        print(" ")
        print("Disk usage is above threshold", (str(disk_threshold)+"%"), "and it's value is: {}%".format(round(disk_percentage, 2)))
        print("Please take necessary measures to make your system function accurately...")
        print("*************************************************************************")
    else:
        print(" ")
        print("The disk usage is stable and it's value is: {}%".format(round(disk_percentage, 2)))
    return timestamp, disk_percentage