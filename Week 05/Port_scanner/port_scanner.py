import socket
import datetime
import subprocess
import platform

def scan_port(host, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0


def count_open_ports(host, start_port, end_port):
    open_count = 0
    log_entries = []
    
    try:
        print(f"Scanning {host} from port {start_port} to {end_port}...")
        for port in range(start_port, end_port + 1):
            if scan_port(host, port):
                open_count += 1
                log_entries.append(f"Port {port}: OPEN")
            else:
                log_entries.append(f"Port {port}: CLOSED")
        
        result_msg = f"Found {open_count} open ports on {host} (ports {start_port}-{end_port})."
        log_entries.insert(0, result_msg)
        print(result_msg)
    
    except Exception as e:
        error_msg = f"Error during scan: {str(e)}"
        log_entries.append(error_msg)
        print(error_msg)
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("port_count_log.txt", "a") as log_file:
        log_file.write(f"[{timestamp}] Scan on {host}:\n")
        for entry in log_entries:
            log_file.write(f"  - {entry}\n")
        log_file.write("\n")
def check_local_open_ports():
    """Run netstat (Windows) or ss (Linux) to list local open ports."""
    try:
        cmd = ['netstat', '-an'] if platform.system() == 'Windows' else ['ss', '-tuln']
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            print("\nLocal open ports (from system command):")
            print(result.stdout.strip())
        else:
            print(f"Error running command: {result.stderr.strip()}")
    except Exception as e:
        print(f"Error checking local ports: {str(e)}")

# Get user inputs
host = input("Enter host to scan (e.g., 127.0.0.1 for localhost): ").strip()
try:
    start_port = int(input("Enter start port (e.g., 1): "))
    end_port = int(input("Enter end port (e.g., 1024): "))
    check_local = input("Check local open ports after scan? (yes/no): ").strip().lower() == 'yes'
except ValueError:
    print("Error: Ports must be numbers.")
    exit()