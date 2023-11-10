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
def get_memory_ram():
        """API endpoint to get memory (RAM) usage."""
        timestamps, ram_usage = memory_service.get_ram_usage_array()
        return jsonify(timestamps=timestamps, ram_usage_history=ram_usage)
    
@app.route('/api/swap')
def get_memory_swap():
        """API endpoint to get memory ( Swap) usage."""
        timestamps, swap_usage = memory_service.get_swap_usage_array()
        return jsonify(timestamps=timestamps, swap_usage_history=swap_usage)



# Add other API endpoints for additional resources

@scheduler.task('interval', id='cpu_get_data', seconds=15, misfire_grace_time=1000)
def actualise_cpu_data():
    cpu_service.calculate_cpu_usage()

@scheduler.task('interval', id='ram_get_data', seconds=15, misfire_grace_time=1000)
def actualise_ram_data():
    memory_service.calculate_ram_usage()

if __name__ == '__main__':
    app.run(debug=True, port=2376)
    

