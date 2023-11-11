import psutil

def collect_process_count():
    process_count = len(psutil.pids())
    return process_count
