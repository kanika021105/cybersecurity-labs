

failed_attempts = {}

log_file = open("login-log.txt", "r")

lines = log_file.readlines()

print("\n--- Suspicious Login Activity ---\n")

for line in lines:

    parts = line.strip().split()

    ip = parts[0]
    status = parts[1]

    if status == "FAILED":

        if ip not in failed_attempts:
            failed_attempts[ip] = 1
        else:
            failed_attempts[ip] += 1


for ip, count in failed_attempts.items():

    print(f"{ip} → Failed Attempts: {count}")

    if count >= 3:
        print(f" ALERT: Possible brute-force attack from {ip}\n")

log_file.close()
