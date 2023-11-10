from flask import Flask, render_template, jsonify
from flask_apscheduler import APScheduler
import psutil
import sqlite3
import time
from threading import Thread

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


## *******  HISTORICAL DATA STORAGE AND VIEWING *********
@app.route('/api/cpu')
def get_cpu_usage():

    cpu_usage = psutil.cpu_percent()
    return jsonify(cpu_usage=cpu_usage)

@app.route('/api/memory')
def get_memory_usage():

    memory_usage = psutil.virtual_memory().percent
    return jsonify(memory_usage=memory_usage)

@app.route('/api/disk')
def get_disk_usage():

    disk_usage = psutil.disk_usage('/').percent
    return jsonify(disk_usage=disk_usage)

@app.route('/api/network')
def get_network_io():

    network_io = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
    return jsonify(network_io=network_io)

@app.route('/historic-data')
def render_historic_data():
    conn = sqlite3.connect('system_metrics.db')
    c = conn.cursor()

    c.execute("SELECT * FROM metrics")
    data = c.fetchall()

    conn.close()

    return render_template('historic_data.html', data=data)

def collect_metrics():
    conn = sqlite3.connect('system_metrics.db')
    c = conn.cursor()

    timestamp = int(time.time())
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    network_io = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
    uptime = psutil.boot_time()
    load_avg = psutil.getloadavg()[0]
    process_count = len(psutil.pids())
    app_response_time = 0.0
    system_logs = ""
    security_events = ""

    c.execute('''INSERT INTO metrics (timestamp, cpu_usage, memory_usage, disk_usage, network_io,
                 uptime, load_avg, process_count, app_response_time, system_logs, security_events)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (timestamp, cpu_usage, memory_usage, disk_usage,
                                                              network_io, uptime, load_avg, process_count,
                                                              app_response_time, system_logs, security_events))

    conn.commit()
    conn.close()

def run_metrics_collection():
    while True:
        print("Collecting metrics...")
        collect_metrics()
        time.sleep(60)

if __name__ == '__main__':
    conn = sqlite3.connect('system_metrics.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS metrics
                 (timestamp INTEGER, cpu_usage REAL, memory_usage REAL, disk_usage REAL, network_io REAL,
                 uptime REAL, load_avg REAL, process_count INTEGER, app_response_time REAL,
                 system_logs TEXT, security_events TEXT)''')

    conn.commit()
    conn.close()

    metrics_thread = Thread(target=run_metrics_collection)
    metrics_thread.start()

    app.run(debug=True, port=2376)
## *******  END HISTORICAL DATA STORAGE AND VIEWING *********