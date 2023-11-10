from flask import Flask, jsonify, request

app = Flask(__name__)

# Import service modules
#import services.cpu_service as cpu_service
import services.memory_service as memory_service
import services.cpu_service as cpu_service


# Sample process monitoring endpoint
@app.route('/process-monitoring', methods=['POST'])
def process_monitoring():
    # Get process details from the request
    process_name = request.json.get('process_name')
    process_id = request.json.get('process_id')

    # Perform process monitoring validation
    if process_name and process_id:
        # Sample validation logic
        if process_name == "my_process" and process_id == 1234:
            # Process monitoring validation successful
            return jsonify({'status': 'success', 'message': 'Process monitoring validation successful.'}), 200
        else:
            # Process monitoring validation failed
            return jsonify({'status': 'error', 'message': 'Process monitoring validation failed.'}), 400
    else:
        # Return error response if process details are missing
        return jsonify({'status': 'error', 'message': 'Process name and ID are required.'}), 400

if __name__ == '__main__':
    app.run(debug=True)