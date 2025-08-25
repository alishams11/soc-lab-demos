from elasticsearch import Elasticsearch
import json
import os

LOG_FILE = "logs/attacks.json"

def export_to_elasticsearch(es_host="http://localhost:9200", index_name="soc-attacks"):
    """
    Export logs from attacks.json to Elasticsearch
    """
    if not os.path.exists(LOG_FILE):
        print("[!] No log file found to export.")
        return

    with open(LOG_FILE, "r") as f:
        data = json.load(f)

    if not data:
        print("[!] Log file is empty.")
        return

    es = Elasticsearch([es_host])

    for event in data:
        try:
            es.index(index=index_name, body=event)
            print(f"[+] Sent to Elasticsearch: {event}")
        except Exception as e:
            print(f"[!] Failed to send to Elasticsearch: {e}")


def export_to_graylog(file_path="logs/graylog_ingest.json"):
    """
    Export logs from attacks.json to a Graylog ingestion file
    """
    if not os.path.exists(LOG_FILE):
        print("[!] No log file found to export.")
        return

    with open(LOG_FILE, "r") as f:
        data = json.load(f)

    if not data:
        print("[!] Log file is empty.")
        return

    with open(file_path, "w") as f:
        for event in data:
            f.write(json.dumps(event) + "\n")

    print(f"[+] Exported logs for Graylog ingestion -> {file_path}")
