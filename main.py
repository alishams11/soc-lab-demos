from core.utils import log_event

if __name__ == "__main__":
   log_event("192.168.1.10", "127.0.0.1", "brute_force", "failed")
   log_event("192.168.1.10", "127.0.0.1", "port_scan", "open")