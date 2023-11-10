from flask import Flask, render_template, jsonify
from flask_apscheduler import APScheduler
import psutil

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
    

# Defining threshold for CPU usage 

@app.route('/cpu-usage')
def cpu_usage():
    cpu_threshold = 50
    cpu_usages = psutil.cpu_percent(interval=1)
    if cpu_usages > cpu_threshold:
        print(" ")
        print("CPU usage is above threshold", cpu_threshold, "and it's value is: {}%".format(cpu_usages))
        print("Please take necessary measures to make your system function accurately...")
        print("*************************************************************************")
    else:
        print(" ")
        print("CPU usage is stable and it's percentage is: {}%".format(cpu_usages))
        print("*************************************************************************")



# Defining threshold for memory usage 

@app.route('/memory-usage')
def mem_usage():
    mem_threshold = 60
    mem_usages = psutil.virtual_memory().used
    mem_total = psutil.virtual_memory().total
    mem_percentage = (mem_usages / mem_total) * 100
    if mem_percentage > mem_threshold:
        print(" ")
        print("Memory usage is above threshold", (str(mem_threshold)+'%'), "and it's value is: {}%".format(round(mem_percentage, 2)))
        print("Please take necessary measures to make your system function accurately...")
        print("*************************************************************************")
    else:
        print(" ")
        print("The memory usage is stable and it's value is: {}%".format(round(mem_percentage, 2)))



# Defining threshold for disk usage 

@app.route('/disk-usage')
def disk_usage():
    disk_threshold = 70
    disk_usages = psutil.disk_usage('/').used
    disk_total = psutil.disk_usage('/').total
    disk_percentage = (disk_usages / disk_total) * 100
    if disk_percentage > disk_threshold:
        print(" ")
        print("Disk usage is above threshold", (str(disk_threshold)+"%"), "and it's value is: {}%".format(round(disk_percentage, 2)))
        print("Please take necessary measures to make your system function accurately...")
        print("*************************************************************************")
    else:
        print(" ")
        print("The disk usage is stable and it's value is: {}%".format(round(disk_percentage, 2)))
        

if __name__ == '__main__':
    app.run(debug=True, port=2376)
