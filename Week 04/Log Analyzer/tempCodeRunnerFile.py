# Write report
with open(report_file, "w") as f:
    f.write("=== Log Analysis Report ===\n")
    f.write(f"Generated on: {datetime.datetime.now()}\n\n")
    f.write(f"INFO logs: {info_count}\n")
    f.write(f"WARNING logs: {warning_count}\n")
    f.write(f"ERROR logs: {error_count}\n\n")
    f.write("Error Details:\n")
    for e in errors:
        f.write(e)

print(f"Report generated successfully → {report_file}")