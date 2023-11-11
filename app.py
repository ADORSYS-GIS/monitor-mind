from flask import Flask, render_template, jsonify
from flask_apscheduler import APScheduler
import psutil
import sqlite3
import time
from threading import Thread
from services import cpu_service, memory_service, disk_usage, network_io, uptime, load_avg, process_count, app_response_time, system_logs, security_events

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

fake_mem = {}

def _collect_metrics():
    timestamp = int(time.time())
    cpu_usage_value = cpu_service.calculate_cpu_usage()
    memory_usage_value = memory_service.collect_memory_usage()
    disk_usage_value = disk_usage.collect_disk_usage()
    network_io_value = network_io.collect_network_io()
    uptime_value = uptime.collect_uptime()
    load_avg_value = load_avg.collect_load_avg()
    process_count_value = process_count.collect_process_count()
    app_response_time_value = app_response_time.collect_app_response_time()
    system_logs_value = system_logs.collect_system_logs()
    security_events_value = security_events.collect_security_events()

    fake_mem[timestamp] = (cpu_usage_value, memory_usage_value, disk_usage_value,
                            network_io_value, uptime_value, load_avg_value, process_count_value,
                            app_response_time_value, system_logs_value, security_events_value)

# Save metrics to database
def save_metrics_to_db():
    conn = sqlite3.connect('system_metrics.db')
    c = conn.cursor()

    for timestamp, metrics in fake_mem.items():
        cpu_usage_value, memory_usage_value, disk_usage_value, network_io_value, uptime_value, load_avg_value, process_count_value, app_response_time_value, system_logs_value, security_events_value = metrics

        c.execute('''INSERT INTO metrics (timestamp, cpu_usage, memory_usage, disk_usage, network_io,
                     uptime, load_avg, process_count, app_response_time, system_logs, security_events)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (timestamp, cpu_usage_value, memory_usage_value,
                                                                  disk_usage_value, network_io_value, uptime_value,
                                                                  load_avg_value, process_count_value,
                                                                  app_response_time_value, system_logs_value,
                                                                  security_events_value))

    conn.commit()
    conn.close()

# Run metrics collection loop
def run_metrics_collection():
    while True:
        print("Collecting metrics...")
        _collect_metrics()
        save_metrics_to_db()
        time.sleep(60)

@app.route('/historic-data')
def render_historic_data():
    conn = sqlite3.connect('system_metrics.db')
    c = conn.cursor()

    c.execute("SELECT * FROM metrics")
    data = c.fetchall()

    conn.close()

    # Convert data to a list of dictionaries
    result = []
    for row in data:
        result.append({
            'timestamp': row[0],
            'cpu_usage': row[1],
            'memory_usage': row[2],
            'disk_usage': row[3],
            'network_io': row[4],
            'uptime': row[5],
            'load_avg': row[6],
            'process_count': row[7],
            'app_response_time': row[8],
            'system_logs': row[9],
            'security_events': row[10]
        })

    # Return data as a JSON response
    return jsonify(result)

if __name__ == '__main__':
    metrics_thread = Thread(target=run_metrics_collection)
    metrics_thread.start()

    app.run(debug=True, port=2376)

## *******  END HISTORICAL DATA STORAGE AND VIEWING *********