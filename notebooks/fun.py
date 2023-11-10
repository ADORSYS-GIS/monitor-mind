import psutil

def get_disk_space():
    partitions = psutil.disk_partitions()
    disk_info = []

    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            disk_info.append({
                'device': partition.device,
                'mountpoint': partition.mountpoint.count,
                'total': usage.total,
                'used': usage.free,
                'free': usage.free,
                'percent': usage.percent
            })
        except PermissionError:
            continue
    return disk_info
disk_space = get_disk_space()

for disk in disk_space:
    print(f"Device: {disk['device']}")
    print(f"Mountpoint: {disk['mountpoint']}")
    print(f"Used: {disk['used']} bytes")
    print(f"Free: {disk['free']} bytes")
    print(f"Percentage Used: {disk['percent']}%")
    print()