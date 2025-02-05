import yaml
import requests
import logging
from flask import Flask, request, jsonify
from time import sleep

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

def load_registry(path='registry/registry.yaml'):
    with open(path, 'r') as f:
        registry = yaml.safe_load(f)
    return registry.get('modules', [])

modules = load_registry()

def call_module(endpoint, payload, retries=3, delay=2):
    for attempt in range(retries):
        try:
            response = requests.post(endpoint, json=payload, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logging.warning(f"Attempt {attempt+1} failed for {endpoint}: {e}")
            sleep(delay)
    return {"error": f"Failed after {retries} retries"}

@app.route('/mosaic', methods=['POST'])
def mosaic_handler():
    input_data = request.json
    aggregated_results = {}
    for module in modules:
        module_name = module.get('name')
        endpoint = module.get('endpoint')
        logging.info(f"Calling {module_name} at {endpoint}")
        result = call_module(endpoint, input_data)
        aggregated_results[module_name] = result
    return jsonify(aggregated_results)

# Optional: an endpoint for dynamic ingestion (Operator can feed concept text)
@app.route('/ingest', methods=['POST'])
def ingest_handler():
    from ingestion.concept_ingestion import analyze_concept
    data = request.json
    concept_text = data.get("concept_text", "")
    try:
        structured_concept = analyze_concept(concept_text)
        return jsonify({"structured_concept": structured_concept})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
