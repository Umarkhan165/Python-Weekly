# Read the log file
with open("D:\Python Weekly\Week 04\Log Analyzer\sample.log", "r") as f:
    lines = f.readlines()
report_path = r"D:\Python Weekly\Week 04\Log Analyzer\report.txt"
info_count = 0
warning_count = 0
error_count = 0
errors = []

for line in lines:
    if "INFO" in line:
        info_count = info_count + 1
    if "WARNING" in line:
        warning_count = warning_count + 1
    if "ERROR" in line:
        error_count = error_count + 1
        errors.append(line)

with open(report_path, "w") as f:
    f.write("=== Log Report ===\n")
    f.write("INFO logs: " + str(info_count) + "\n")
    f.write("WARNING logs: " + str(warning_count) + "\n")
    f.write("ERROR logs: " + str(error_count) + "\n\n")
    f.write("Error Details:\n")
    for e in errors:
        f.write(e)

print("Report created successfully → report.txt")
