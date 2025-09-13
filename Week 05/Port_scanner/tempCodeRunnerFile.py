import subprocess , platform



cmd = ['netstat', '-an'] if platform.system() == 'Windows' else ['ss', '-tuln']
result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
if result.returncode == 0:
    print("\nLocal open ports (from system command):")
    print(result.stdout.strip())
else:
    print(f"Error running command: {result.stderr.strip()}")

