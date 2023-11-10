import psutil

# Get the RAM usage
ram = psutil.virtual_memory()
ram_total = ram.total
ram_used = ram.used
ram_percent = ram.percent

print(f"RAM Total: {ram_total} bytes")
print(f"RAM Used: {ram_used} bytes")
print(f"RAM Percent: {ram_percent}%")

# Get the SWAP usage
swap = psutil.swap_memory()
swap_total = swap.total
swap_used = swap.used
swap_percent = swap.percent

print(f"SWAP Total: {swap_total} bytes")
print(f"SWAP Used: {swap_used} bytes")
print(f"SWAP Percent: {swap_percent}%")