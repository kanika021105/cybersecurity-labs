import hashlib
import os
from datetime import datetime

BASELINE_FILE = "baseline.txt"
MONITOR_DIR = "monitored-files"


def calculate_hash(filepath):
    with open(filepath, "rb") as file:
        return hashlib.sha256(file.read()).hexdigest()


# Get current timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Store current file hashes
current_hashes = {}

for filename in os.listdir(MONITOR_DIR):

    filepath = os.path.join(MONITOR_DIR, filename)

    if os.path.isfile(filepath):

        current_hashes[filename] = calculate_hash(filepath)


# First run: create baseline
if not os.path.exists(BASELINE_FILE):

    with open(BASELINE_FILE, "w") as baseline:

        for file, hash_value in current_hashes.items():

            baseline.write(f"{file}:{hash_value}\n")

    print("✅ Baseline Created")

else:

    stored_hashes = {}

    modified_files = []
    new_files = []
    deleted_files = []

    # Load baseline hashes
    with open(BASELINE_FILE, "r") as baseline:

        for line in baseline:

            if ":" in line:

                file, hash_value = line.strip().split(":", 1)

                stored_hashes[file] = hash_value

    print("\n===== FILE INTEGRITY REPORT =====\n")

    # Check current files
    for file, current_hash in current_hashes.items():

        if file in stored_hashes:

            if current_hash == stored_hashes[file]:

                print(f"[{timestamp}]  {file} : Integrity Verified")

            else:

                print(f"[{timestamp}]  {file} : File Modified")

                modified_files.append(file)

        else:

            print(f"[{timestamp}]  {file} : New File Detected")

            new_files.append(file)

    # Check deleted files
    for file in stored_hashes:

        if file not in current_hashes:

            print(f"[{timestamp}]  {file} : File Deleted")

            deleted_files.append(file)

    # Generate report
    with open("security-report.txt", "w") as report:

        report.write("===== SECURITY AUDIT REPORT =====\n\n")

        report.write(f"Generated: {timestamp}\n\n")

        report.write("Modified Files:\n")

        if modified_files:

            for file in modified_files:

                report.write(f"- {file}\n")

        else:

            report.write("None\n")

        report.write("\nDeleted Files:\n")

        if deleted_files:

            for file in deleted_files:

                report.write(f"- {file}\n")

        else:

            report.write("None\n")

        report.write("\nNew Files:\n")

        if new_files:

            for file in new_files:

                report.write(f"- {file}\n")

        else:

            report.write("None\n")

    print("\n Security report generated: security-report.txt")
