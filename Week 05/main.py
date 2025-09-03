import subprocess
import time


comnd = "node main.js"
# comnd = "python example.py"
time.sleep(3)

subprocess.call(comnd)
print("File Executed!")