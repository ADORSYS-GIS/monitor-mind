from time import time


def get_history_time():
    """Return the history of time."""
    timestamp = time()
    return int(timestamp * 1000)
