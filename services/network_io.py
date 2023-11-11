import psutil

def collect_network_io():
    network_io = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
    return network_io
