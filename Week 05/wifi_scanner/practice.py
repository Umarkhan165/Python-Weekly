import subprocess
import datetime
import re


log_entries = []
devices = []

def scan():
    result = subprocess.run(['arp', '-a'], capture_output=True, text=True, timeout=5)
    print(result)
    if result.returncode != 0:
        raise Exception(f"ARP command failed: {result.stderr.strip()}")

        output_lines = result.stdout.splitlines()
        print(result)
        for line in output_lines:
                # Match lines with IP and MAC (e.g., "192.168.1.1  00-14-22-01-23-45  dynamic")
                match = re.match(r'\s*(\d+\.\d+\.\d+\.\d+)\s+([0-9A-Fa-f-]{17})\s+(\w+)', line)
                if match:
                    ip, mac, type_ = match.groups()
                    devices.append({'ip': ip, 'mac': mac, 'type': type_})
        
        if not devices:
            log_entries.append("No devices found in ARP cache.")
            print("No devices found in ARP cache.")
        else:
            log_entries.append(f"Found {len(devices)} devices:")
            print(f"Found {len(devices)} devices:")
            for device in devices:
                entry = f"IP: {device['ip']}, MAC: {device['mac']}, Type: {device['type']}"
                log_entries.append(entry)
                print(entry)
        