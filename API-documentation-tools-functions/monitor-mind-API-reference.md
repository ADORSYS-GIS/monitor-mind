# Monitormind provides the following  functionalities

- **CPU Monitoring**: Real-time monitoring of CPU usage.
- **Memory Monitoring**: Track RAM and swap usage.
- **Process Tracking**: Monitor and display active system processes.
- **Real-Time Updates**: Frontend updates using polling to display the latest data.

It does this by using the flask Advance Scheduler to schedule code to be executed whenever the client wants to monitor something.
Monitor mind also uses python system and process utilities (psutils) to retrieve information on running processes and system utilisation.


Monitormind also makes use of RESTAPI services which lets it interact the client's software using HTTP request such as GET, POST, PATCH AND HEAD.


#  The api code or controller

# starts by importing all necessary packages
from flask import Flask, render_template, jsonify
from flask_apscheduler import APScheduler

# Import service modules
import services.cpu_service as cpu_service
import services.memory_service as memory_service



# set configuration values. The APScheduler is used here to schedule job which will be executed whenever a get request is recived. 
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

# code bloc to display the home page.
@app.route('/')
def home():
    """Serve the homepage with system metrics."""
    return render_template('index.html')


# Code bloc to monitor cpu usage. It uses a get request and then displays data in Java Script Object Notation(JSON)
@app.route('/api/cpu')
def get_cpu():
    """API endpoint to get CPU usage."""
    timestamps, cpu_usage = cpu_service.get_cpu_usage_array()
    return jsonify(timestamps=timestamps, cpu_usage=cpu_usage)

# RAM and swap tracking code
@app.route('/api/memory')
def get_memory():
    """API endpoint to get memory (RAM and Swap) usage."""
    ram_usage, swap_usage = memory_service.get_memory_usage()
    return jsonify(ram_usage_history=ram_usage, swap_usage_history=swap_usage)


# code bloc to monitor and display system process
@app.route('/api/process')
def get_processes():
    """API endpoint to get active processes."""
       active_processes 

@scheduler.task('interval', id='cpu_get_data', seconds=15, misfire_grace_time=1000)
def actualise_cpu_data():
    cpu_service.calculate_cpu_usage()


if __name__ == '__main__':
    app.run(debug=True, port=2376)
