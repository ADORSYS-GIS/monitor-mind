import psutil

def collect_uptime():
    uptime = psutil.boot_time()
    return uptime
