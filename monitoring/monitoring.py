import time
import logging
import requests
from datetime import datetime

def monitor_endpoint(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return True, response.elapsed.total_seconds()
    except Exception as e:
        return False, str(e)

def monitor_all(endpoints):
    results = {}
    for name, url in endpoints.items():
        status, info = monitor_endpoint(url)
        results[name] = {"status": status, "info": info, "timestamp": datetime.utcnow().isoformat()}
    return results

if __name__ == "__main__":
    endpoints = {
        "mosaic_engine": "http://localhost:5000/mosaic",
        "task_manager": "http://localhost:6001/process",
        "client_crm": "http://localhost:6002/process"
    }
    while True:
        result = monitor_all(endpoints)
        logging.info(result)
        time.sleep(60)
