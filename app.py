from flask import Flask, render_template, jsonify
from flask_apscheduler import APScheduler
import psutil
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
from prometheus_client import push_to_gateway

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

# defining prometheus metrics.

cpu_usage = Gauge('cpu_usage', 'CPU usage')
mem_usage = Gauge('mem_usage', 'Memory usage')
disk_usage = Gauge('disk_usage', 'Disk usage')
network_traffic = Gauge('network_traffic', 'Network traffic')
system_uptime = Gauge('system_uptime', 'System timeup')
load_average = Gauge('load_average', 'Load average')
process_count = Gauge('process_count', 'Process count')
app_response_times = Gauge('app_response_times', 'Application response time')
system_logs = Gauge('system_logs', 'System logs')
security_events = Gauge('security_events', 'Security events')

@app.route('/historic-metrics')
# update prometheus metrics from collected metrics
def collectd_metrics():
    cpu_percentage = psutil.cpu_percent()
    cpu_usage.set(cpu_percentage)

    mem_percentage = psutil.virtual_memory().percent # does this line have any mistakes?????
    mem_usage.set(mem_percentage)

    disk_percentage = psutil.disk_usage('/').percent
    disk_usage.set(disk_percentage)

    network_bytes_sent = psutil.net_io_counters().bytes_sent
    network_bytes_recv = psutil.net_io_counters().bytes_recv
    network_traffic.set(network_bytes_sent + network_bytes_recv)

    uptime_seconds = psutil.boot_time()
    system_uptime.set(uptime_seconds)

    load_avg_1min, _, _ = psutil.getloadavg()
    load_average.set(load_avg_1min)

    process_count_value = len(psutil.pids())
    process_count.set(process_count_value)

    app_response_times.set(0.5) # assumes a response time of 0.5s

    system_logs.set(10) # assumes 10 system logs recorded

    security_events.set(5) # assumes 5 security events recorded

    # Store metrics in Prometheus
    registry = CollectorRegistry()
    registry.register(cpu_usage)
    registry.register(mem_usage)
    registry.register(disk_usage)
    registry.register(network_traffic)
    registry.register(system_uptime)
    registry.register(load_average)
    registry.register(process_count)
    registry.register(app_response_times)
    registry.register(system_logs)
    registry.register(security_events)

    push_to_gateway('localhost:2376', job='my_job', registry=registry)

    # Query Prometheus metrics and retrieve historic data
    cpu_query = requests.get('http://127.0.0.1:2376/historic-metrics', params={'query': 'cpu_usage'})
    cpu_data = cpu_query.json()['data']['result']

    mem_query = requests.get('http://127.0.0.1:2376/historic-metrics', params={'query': 'mem_usage'})
    mem_data = mem_query.json()['data']['result']

    disk_query = requests.get('http://127.0.0.1:2376/historic-metrics', params={'query': 'disk_usage'})
    disk_data = disk_query.json()['data']['result']

    network_query = requests.get('http://127.0.0.1:2376/historic-metrics', params={'query': 'network_traffic'})
    network_data = network_query.json()['data']['result']

    uptime_query = requests.get('http://127.0.0.1:2376/historic-metrics', params={'query': 'system_uptime'})
    uptime_data = uptime_query.json()['data']['result']

    loadavg_query = requests.get('http://127.0.0.1:2376/historic-metrics', params={'query': 'load_average'})
    loadavg_data = loadavg_query.json()['data']['result']

    processcount_query = requests.get('http://127.0.0.1:2376/historic-metrics', params={'query': 'process_count'})
    processcount_data = processcount_query.json()['data']['result']

    appresponse_query = requests.get('http://127.0.0.1:2376/historic-metrics', params={'query': 'app_response_times'})
    appresponse_data = appresponse_query.json()['data']['result']

    systemlogs_query = requests.get('http://127.0.0.1:2376/historic-metrics', params={'query': 'system_logs'})
    systemlogs_data = systemlogs_query.json()['data']['result']

    securityevents_query = requests.get('http://127.0.0.1:2376/historic-metrics', params={'query': 'security_events'})
    securityevents_data = securityevents_query.json()['data']['result']

    return render_template('historic_data.html', cpu_data=cpu_data, mem_data=mem_data, disk_data=disk_data,
                        network_data=network_data, uptime_data=uptime_data, loadavg_data=loadavg_data,
                        processcount_data=processcount_data, appresponse_data=appresponse_data,
                        systemlogs_data=systemlogs_data, securityevents_data=securityevents_data)


## *******  END HISTORICAL DATA STORAGE AND VIEWING *********

if __name__ == '__main__':
    app.run(debug=True, port=2376)
