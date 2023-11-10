
# MonitorMind: Automated System Monitoring Tool

## Overview
MonitorMind is an automated system monitoring tool designed to provide real-time insights into various system metrics such as CPU usage, RAM, Swap usage, and system processes. Developed as a Flask web application, MonitorMind utilizes Python's `psutil` library to gather system data, presenting it in a user-friendly web interface.

## Key Features
- **CPU Monitoring**: Real-time monitoring of CPU usage.
- **Memory Monitoring**: Track RAM and swap usage.
- **Process Tracking**: Monitor and display active system processes.
- **Real-Time Updates**: Frontend updates using polling to display the latest data.
- **User-Friendly Dashboard**: A simple and intuitive web interface for viewing system metrics.

## Installation

```bash
git clone https://github.com/ADORSYS-GIS/monitor-mind
cd monitor-mind
```

## Usage

Run the Flask application:

```bash
python3 app.py
```

-- or --

```bash
flask run
```

Navigate to the provided local server address in your web browser to view the monitoring dashboard.

## System Monitoring tools Detail Documentation
Check out this Document [smtdoc](smtdoc/system_monitoring_tools.md)

## System Data Retrieval

MonitorMind uses the `psutil` library to retrieve system data:

- **CPU Usage**: `psutil.cpu_percent(interval=1)`
- **Memory Usage**: `psutil.virtual_memory()`
- **Swap Usage**: `psutil.swap_memory()`
- **System Processes**: `psutil.process_iter(attrs=['pid', 'name'])`

## Contributing

We welcome contributions to MonitorMind. Please read our contributing guidelines before submitting pull requests.

## Acknowledgements

Special thanks to all the contributors and students involved in this project for their hard work and dedication.

## License

This project is licensed under the [MIT License](LICENSE).
