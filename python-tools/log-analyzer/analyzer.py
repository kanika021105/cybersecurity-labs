log_file = open("sample-log.txt", "r")

lines = log_file.readlines()

warning_count = 0
error_count = 0

print("\n--- Suspicious Log Entries ---\n")

for line in lines:

    if "WARNING" in line:
        warning_count += 1
        print("[WARNING]", line.strip())

    elif "ERROR" in line:
        error_count += 1
        print("[ERROR]", line.strip())

print("\n--- Summary ---")
print(f"Warnings Detected: {warning_count}")
print(f"Errors Detected: {error_count}")

log_file.close()
