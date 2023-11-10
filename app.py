from flask import Flask, render_template, jsonify
from flask_apscheduler import APScheduler
from services.ram_swap import collect_swap_ram_usage

# Import service modules
import services.cpu_service as cpu_service
import services.memory_service as memory_service
import os
import datetime
import time
import psutil


# Add other necessary imports here

# set configuration values
class Config:
    SCHEDULER_API_ENABLED = True


# create app
app = Flask(__name__)
app.config.from_object(Config())

# initialize scheduler
scheduler = APScheduler()
# if you don't wanna use a config, you can set options here:
# scheduler.api_enabled = True
scheduler.init_app(app)
scheduler.start()


@app.route('/')
def home():
    """Serve the homepage with system metrics."""
    return render_template('index.html')


@app.route('/api/cpu')
def get_cpu():
    """API endpoint to get CPU usage."""
    timestamps, cpu_usage = cpu_service.get_cpu_usage_array()
    return jsonify(timestamps=timestamps, cpu_usage=cpu_usage)


@app.route('/api/memory')
def get_memory():
    """API endpoint to get memory (RAM and Swap) usage."""
    ram_usage, swap_usage = memory_service.get_memory_usage()
    return jsonify(ram_usage_history=ram_usage, swap_usage_history=swap_usage)

def get_home_directory():
    """Get the home directory of the user."""
    return os.path.expanduser("~")

def create_log_file():
# Create the log file in the home directory if it doesn't exist.
    log_file_path = os.path.join(get_home_directory(), "ram_swap_usage.log")
    if not os.path.exists(log_file_path):
        with open(log_file_path, "w") as file:
            file.write("Timestamp, RAM Usage (%), Swap Usage (%)\n")
    return log_file_path

log_file_path = create_log_file()

#Route to collect and start storing the log data of the SWAP and RAM files
@app.route('/collect')
def start_collection():
    while True:
        ram_usage, swap_usage = collect_swap_ram_usage()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp}, {ram_usage}, {swap_usage}\n"
        with open(log_file_path, "a") as file:
            file.write(log_entry)
            file.flush()
        time.sleep(1)  # Adjust the sleep duration as per your requirements
    return "RAM and Swap usage collection started!"

# Add other API endpoints for additional resources

@scheduler.task('interval', id='cpu_get_data', seconds=15, misfire_grace_time=1000)
def actualise_cpu_data():
    cpu_service.calculate_cpu_usage()


if __name__ == '__main__':
    app.run(debug=True, port=2376)
