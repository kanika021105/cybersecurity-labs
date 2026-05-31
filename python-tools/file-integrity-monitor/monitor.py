import hashlib
import os

BASELINE_FILE = "baseline.txt"
MONITOR_DIR = "monitored-files"


def calculate_hash(filepath):

    with open(filepath, "rb") as file:
        return hashlib.sha256(file.read()).hexdigest()


current_hashes = {}

for filename in os.listdir(MONITOR_DIR):

    filepath = os.path.join(MONITOR_DIR, filename)

    if os.path.isfile(filepath):

        current_hashes[filename] = calculate_hash(filepath)

# First Run
if not os.path.exists(BASELINE_FILE):

    with open(BASELINE_FILE, "w") as baseline:

        for file, hash_value in current_hashes.items():
            baseline.write(f"{file}:{hash_value}\n")

    print(" Baseline Created")

else:

    stored_hashes = {}

    with open(BASELINE_FILE, "r") as baseline:

        for line in baseline:

            file, hash_value = line.strip().split(":")
            stored_hashes[file] = hash_value

    print("\n===== FILE INTEGRITY REPORT =====\n")

    for file, current_hash in current_hashes.items():

        if file in stored_hashes:

            if current_hash == stored_hashes[file]:

                print(f" {file} : Integrity Verified")

            else:

                print(f" {file} : File Modified")
  
