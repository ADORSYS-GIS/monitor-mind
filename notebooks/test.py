import psutil


def get_disk_space():
    partitions = psutil.disk_partitions()
    disk_info = []
    # This portion of the code is used to check Disk Usage and Availability Information
    # Check Disk Usage Information
    print("                       ")
    print("Disk Usage Information") 
    print("------------------------")
    disk_usage = psutil.disk_usage('/')
    print(f"Total: {disk_usage.total}")
    print(f"Used: {disk_usage.used}")
    print(f"Free: {disk_usage.free}")
    print(f"Percentage Used: {disk_usage.percent}%")

    return disk_info
disk_space = get_disk_space()

# Check Disk Availability Information
print("                             ")
print("Disk Availability Information")
print("------------------------------")
disk_avail = psutil.disk_partitions()
for partition in disk_avail:
    print(f"Device: {partition.device}")
    print(f"Mountpoint: {partition.mountpoint}")
    print(f"Filesystem: {partition.fstype}")
    print(f"Options: {partition.opts}")
    print("----------------------------------------------------------------------------")