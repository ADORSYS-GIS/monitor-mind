import psutil
import time

# Function to track and report running processes
def track_processes():
    while True:
        running_processes = []
        for process in psutil.process_iter(['pid', 'name']):
            running_processes.append({'pid': process.info['pid'], 'name': process.info['name']})
        print("Running Processes:")
        for process in running_processes:
            print(f"PID: {process['pid']}, Name: {process['name']}")
        print("--------------------------------------------")
        time.sleep(1)  # Wait for 5 seconds before rechecking the processes

# Main program
if __name__ == '__main__':
    # Call the function to continuously track and report running processes
    track_processes()
