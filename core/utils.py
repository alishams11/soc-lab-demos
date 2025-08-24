import json
from datetime import datetime
import os

LOG_FILE = "logs/attacks.json"

def log_event(source_ip, destination_ip, attack_type, status):
    
    event = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "source_ip": source_ip,
        "destination_ip": destination_ip,
        "attack_type": attack_type,
        "status": status
    }

    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            json.dump([], f, indent=4)

    with open(LOG_FILE, "r") as f:
        data = json.load(f)

    data.append(event)

    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=4)

    print(f"[+] Logged event: {event}")

