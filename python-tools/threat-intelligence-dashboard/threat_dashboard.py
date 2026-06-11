high_risk_ips = [
    "185.220.101.1",
    "45.33.32.156"
]

medium_risk_ips = [
    "8.8.8.8"
]

with open("threats.txt", "r") as file:

    ips = file.readlines()

high = 0
medium = 0
low = 0

report = []

print("\n===== THREAT INTELLIGENCE REPORT =====\n")

for ip in ips:

    ip = ip.strip()

    if ip in high_risk_ips:

        print(f"[HIGH] {ip}")

        report.append(f"[HIGH] {ip}\n")

        high += 1

    elif ip in medium_risk_ips:

        print(f"[MEDIUM] {ip}")

        report.append(f"[MEDIUM] {ip}\n")

        medium += 1

    else:

        print(f"[LOW] {ip}")

        report.append(f"[LOW] {ip}\n")

        low += 1

print("\n===== SUMMARY =====\n")

print(f"HIGH: {high}")
print(f"MEDIUM: {medium}")
print(f"LOW: {low}")

with open("threat-report.txt", "w") as file:

    file.writelines(report)

print("\n Threat report generated")
