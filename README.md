📘 SOC Lab Demos
🎯 Project Goal

This project is a simulation lab for attacks and log generation to practice in a Security Operations Center (SOC) environment.
It allows you to simulate basic attacks like Brute-force and Port Scan, and generate logs that can be analyzed in ELK or Graylog.

#📂 Project Structure
soc-lab-demos/
├── attacks/
│   ├── brute_force.py       # Simulate brute-force on SSH
│   └── port_scan.py         # Simulate port scanning
├── core/
│   ├── utils.py             # Log formatting
│   └── exporter.py          # Export logs to ELK/Graylog
├── logs/                    # Stored logs
├── screenshots/             # Execution screenshots
├── main.py                  # CLI entrypoint
├── README.md
├── requirements.txt
└── LICENSE

#⚙️ Installation
1. Clone the repository
git clone git@github.com:alishams11/soc-lab-demos.git
cd soc-lab-demos

2. Create a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

#🚀 Usage
Run attacks:

Brute-force simulation:
python3 main.py --attack brute_force

Port scan simulation:
python3 main.py --attack port_scan

Export logs:

Send to Elasticsearch (requires ELK server):
python3 main.py --export elk

Export to file for Graylog ingestion:
python3 main.py --export file

#📄 Logs
All logs are saved under the logs/ folder.
Logs are formatted in JSON with the following fields:
{
  "timestamp": "2025-08-16T14:25:01",
  "source_ip": "192.168.1.10",
  "destination_ip": "192.168.1.20",
  "attack_type": "brute_force",
  "status": "failed"
}

#🖼️ Example Execution
Screenshots of the tool running are available in the screenshots/ folder.
Sample terminal output:
[*] Running brute-force simulation...
[+] Attempt admin:password123 -> Failed
[+] Attempt root:toor -> Failed
[+] Log saved to logs/brute_force.log

#📌 Future Roadmap

Add more attack modules (SQLi, XSS, DoS)

Support for additional SIEM solutions

Automated log analysis
