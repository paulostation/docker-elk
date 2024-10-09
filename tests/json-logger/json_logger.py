# json-logger/json_logger.py
import json
import time
import random

# Generate sample logs in JSON format
while True:
    log = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "level": "INFO",
        "message": "This is a JSON formatted log",
        "value": random.randint(1, 100)
    }
    print(json.dumps(log))
    time.sleep(2)
