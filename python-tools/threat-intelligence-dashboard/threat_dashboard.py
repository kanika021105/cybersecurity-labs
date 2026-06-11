import json
import csv
from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

high = 0
medium = 0
low = 0

report = []
csv_data = []

print("\n===== THREAT INTELLIGENCE REPORT =====\n")

with open("threats.json", "r") as file:

    threats = json.load(file)

for threat in threats:

    ip = threat["ip"]
    risk = threat["risk"]

    if risk == "HIGH":

        score = 90

        high += 1

    elif risk == "MEDIUM":

        score = 60

        medium += 1

    else:

        score = 20

        low += 1

    print(
        f"[{timestamp}] [{risk}] {ip} | Threat Score: {score}"
    )

    report.append(
        f"[{timestamp}] [{risk}] {ip} | Threat Score: {score}\n"
    )

    csv_data.append(
        [
            timestamp,
            ip,
            risk,
            score
        ]
    )

print("\n===== DASHBOARD SUMMARY =====\n")

print(f"HIGH: {high}")
print(f"MEDIUM: {medium}")
print(f"LOW: {low}")

total = high + medium + low

print(f"\nTotal IPs Analysed: {total}")


with open("threat-report.txt", "w") as file:

    file.writelines(report)


with open(
    "threat-report.csv",
    "w",
    newline=""
) as csvfile:

    writer = csv.writer(csvfile)

    writer.writerow(
        [
            "Timestamp",
            "IP Address",
            "Risk",
            "Threat Score"
        ]
    )

    writer.writerows(csv_data)

print("\n threat-report.txt generated")
print(" threat-report.csv generated")
