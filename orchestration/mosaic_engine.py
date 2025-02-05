import yaml
import requests
import logging
from flask import Flask, request, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

def load_registry(path='registry/registry.yaml'):
    with open(path, 'r') as f:
        registry = yaml.safe_load(f)
    return registry.get('modules', [])

modules = load_registry()

@app.route('/mosaic', methods=['POST'])
def mosaic_handler():
    input_data = request.json
    aggregated_results = {}

    # Optionally, insert AI logic here to determine call order or filtering.
    for module in modules:
        module_name = module.get('name')
        endpoint = module.get('endpoint')
        try:
            logging.info(f"Calling {module_name} at {endpoint}")
            response = requests.post(endpoint, json=input_data, timeout=10)
            response.raise_for_status()
            aggregated_results[module_name] = response.json()
        except Exception as e:
            logging.error(f"Error calling {module_name}: {str(e)}")
            aggregated_results[module_name] = {'error': str(e)}
    return jsonify(aggregated_results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
