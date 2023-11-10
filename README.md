Python Process Monitoring

Objective1: Explore ways to list and monitor running processes in python.

This documentation provides a step-by-step guide on how to list and monitor processes in your system using Python and Flask. Flask is a popular web framework that allows you to build web applications efficiently.

## Prerequisites

Before you begin, ensure that you have the following installed:

- Python: Make sure you have Python installed on your system. 

- Flask: Install Flask using pip, the Python package installer. 
  ````bash
  pip install flask
  ```

Once you have the prerequisites ready, you can proceed with the following steps:

## Step 1: Create a Flask Application

Create a new Python file, e.g., `app.py`, and import the necessary modules:

```python
from flask import Flask, jsonify
import psutil
```

Initialize the Flask application:

```python
app = Flask(__name__)
```

## Step 2: Define API Endpoints

Define the API endpoints that will list and monitor the processes. In this example, we will create two endpoints: one to list all running processes and another to monitor the CPU usage of a specific process.

### Endpoint to List Running Processes

```python
@app.route('/processes', methods=['GET'])
def get_processes():
    process_list = []
    for process in psutil.process_iter():
        process_list.append({'pid': process.pid, 'name': process.name()})
    return jsonify(process_list)
```

### Endpoint to Monitor CPU Usage of a Process

```python
@app.route('/processes/<int:pid>/cpu', methods=['GET'])
def get_cpu_usage(pid):
    process = psutil.Process(pid)
    cpu_percent = process.cpu_percent(interval=1)
    return jsonify({'pid': pid, 'cpu_percent': cpu_percent})
```

## Step 3: Run the Flask Application

Add the following lines at the end of your `app.py` file to run the Flask application:

```python
if __name__ == '__main__':
    app.run(debug=True)
```

## Step 4: Start the Flask Server

Open your terminal or command prompt, navigate to the directory containing your `app.py` file, and run the following command:

```bash
python app.py
```

The Flask server will start running on your local machine.

## Conclusion
 You have successfully created a Flask application that lists and monitors processes in your system. 
 
 

 
 # Process Monitoring Test 

How to implement tests to validate process monitoring functionality in your Python application. 

## Step 1: Create a Test File

Create a new Python file, e.g., `test_process_monitoring.py`, to contain your tests.

Import the necessary modules:

```python
import unittest
import psutil
```

## Step 2: Define Test Cases

Define the test cases to validate the process monitoring functionality. Each test case should focus on specific aspects of the process monitoring code.

Create a test class that inherits from `unittest.TestCase`:

```python
class ProcessMonitoringTestCase(unittest.TestCase):
    def test_process_list_not_empty(self):
        # Test that the process list is not empty
        processes = psutil.process_iter()
        self.assertTrue(len(list(processes)) > 0)

    def test_cpu_usage_valid(self):
        # Test that the CPU usage of a process is within a valid range
        pid = 1234  # Replace with the actual process ID to test
        process = psutil.Process(pid)
        cpu_percent = process.cpu_percent(interval=1)
        self.assertGreaterEqual(cpu_percent, 0)
        self.assertLessEqual(cpu_percent, 100)
```

In the above example, we have two test cases: `test_process_list_not_empty` and `test_cpu_usage_valid`. Adjust the test cases based on your specific process monitoring requirements.

## Step 3: Run the Tests

Add the following lines at the end of your test file to run the tests:

```python
if __name__ == '__main__':
    unittest.main()
```

## Step 4: Run the Tests

Open your terminal or command prompt, navigate to the directory containing your test file, and run the following command:

```bash
python test_process_monitoring.py
```
# Conclusion 

We were able to write document a python script which will list, monitor and test to validate process monitoring.