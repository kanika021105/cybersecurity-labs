import hashlib

def calculate_hash(filename):

    with open(filename, "rb") as file:
        data = file.read()

    return hashlib.sha256(data).hexdigest()


filename = "testfile.txt"

current_hash = calculate_hash(filename)

try:

    with open("baseline.txt", "r") as baseline:
        stored_hash = baseline.read()

    if current_hash == stored_hash:

        print("✅ File Integrity Verified")

    else:

        print("🚨 ALERT: File Has Been Modified")

except FileNotFoundError:

    with open("baseline.txt", "w") as baseline:
        baseline.write(current_hash)

    print("Baseline Created Successfully")
