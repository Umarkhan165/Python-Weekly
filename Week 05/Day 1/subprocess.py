import subprocess
import time


# comnd = "node main.js"
# # comnd = "python example.py"
# time.sleep(3)

# subprocess.call(comnd)
# print("File Executed!")

# subprocess.run(["dir"], shell=True)

# It is also used for opening and closing program.
# subprocess.run("Notepad")

#  3. Capturing command output
# result= subprocess.run(["echo", "HEllo world"] ,capture_output=True , text=True)
# print("Output:", result.stdout)


# Handling Errors

# try:
#     subprocess.run(["wrong_command"], check=True)
# except subprocess.CalledProcessError:
#     print("COmmadn Not Valid")

# For Ping check

# import subprocess

# process = subprocess.Popen(["ping", "google.com"], stdout=subprocess.PIPE, text=True)

# for line in process.stdout:
#     print(line.strip())  # Prints ping results in real time

# Work with Other Tools
# Control Git, Docker, FFmpeg, etc. from Python.
# result = subprocess.run(["git", "status"], capture_output=True, text=True)
# print(result.stdout)



# Moving A file
# move old.txt to new.txt 
# Above oen is used for transfering the files inside windwos terminal
# subprocess.run(["move","D:\C++\main.py", "D:\Python Weekly\Week 05\main.py"] , shell=True) 
# Moves file form one destination to Another one.


# Copy a file
# subprocess.run(["copy","D:\Python Weekly\Week 05\main.py", "D:\C++"] , shell=True)

# subprocess.run(["del", "Python Weekly\Week 05\new.txt"], shell=True)

# Use teh above commadn correcty "Warning"

# For running other scripts:

# subprocess.run(["python", "D:\Python Weekly\Week 05\example.py"])

# Output: 
#   subprocess.run(["python", "D:\Python Weekly\Week 05\example.py"])
# HEllo boi


# Run a Batch/PowerShell Script (Windows)

subprocess.run(["shell.bash"], shell=True)