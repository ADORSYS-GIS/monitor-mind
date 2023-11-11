import psutil

def collect_load_avg():
    load_avg = psutil.getloadavg()[0]
    return load_avg
