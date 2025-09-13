import subprocess
import datetime
import re

def scan_network():
    log_entries = []
    devices = []
    
    try:

        result = subprocess.run(['arp', '-a'], capture_output=True, text=True, timeout=5)
        
        if result.returncode != 0:
            raise Exception(f"ARP command failed: {result.stderr.strip()}")
        
        output_lines = result.stdout.splitlines()
        for line in output_lines:
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
        
    except subprocess.TimeoutExpired:
        error_msg = "Timeout while running arp -a"
        log_entries.append(error_msg)
        print(error_msg)
    except Exception as e:
        error_msg = f"Error during network scan: {str(e)}"
        log_entries.append(error_msg)
        print(error_msg)
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("network_scan_log.txt", "a") as log_file:
        log_file.write(f"[{timestamp}] Network Scan:\n")
        for entry in log_entries:
            log_file.write(f"  - {entry}\n")
        log_file.write("\n")


scan_network()