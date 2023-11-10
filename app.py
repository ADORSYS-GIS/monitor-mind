from flask import Flask, render_template, jsonify
from flask_apscheduler import APScheduler

# Import service modules
import services.cpu_service as cpu_service
import services.memory_service as memory_service


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


# Add other API endpoints for additional resources

@scheduler.task('interval', id='cpu_get_data', seconds=15, misfire_grace_time=1000)
def actualise_cpu_data():
    cpu_service.calculate_cpu_usage()
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

if __name__ == '__main__':
    app.run(debug=True, port=2376)
