import argparse
from attacks import brute_force, port_scan
from core import exporter

def main():
    parser = argparse.ArgumentParser(description="SOC Lab Demo CLI")
    parser.add_argument("--attack", choices=["brute_force", "port_scan"], help="Choose an attack to simulate")
    parser.add_argument("--export", choices=["elk", "file"], help="Export logs to ELK or Graylog")

    args = parser.parse_args()

    if args.attack == "brute_force":
        print("[*] Running brute-force simulation...")
        brute_force.run()
    elif args.attack == "port_scan":
        print("[*] Running port scan simulation...")
        port_scan.run()

    if args.export == "elk":
        print("[*] Exporting logs to Elasticsearch...")
        exporter.export_to_elasticsearch()
    elif args.export == "file":
        print("[*] Exporting logs for Graylog ingestion...")
        exporter.export_to_graylog()

if __name__ == "__main__":
    main()
