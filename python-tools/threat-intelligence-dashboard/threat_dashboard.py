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

# Search Filter

risk_filter = input(
    "Filter by risk (HIGH/MEDIUM/LOW/ALL): "
).upper()

filtered_threats = []

for threat in threats:

    if risk_filter == "ALL":

        filtered_threats.append(threat)

    elif threat["risk"] == risk_filter:

        filtered_threats.append(threat)

for threat in filtered_threats:

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

# Top Threats

print("\n===== TOP THREATS =====\n")

for threat in filtered_threats:

    if threat["risk"] == "HIGH":

        print(threat["ip"])

# Text Report

with open(
    "threat-report.txt",
    "w"
) as file:

    file.writelines(report)

# CSV Report

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

# HTML Dashboard

html = f"""
<!DOCTYPE html>

<html>

<head>

<title>Threat Intelligence Dashboard</title>

<style>

body {{
    font-family: Arial;
    margin: 40px;
}}

table {{
    border-collapse: collapse;
    width: 100%;
}}

th, td {{
    border: 1px solid #ddd;
    padding: 10px;
}}

th {{
    background-color: #f2f2f2;
}}

.high {{
    color: red;
    font-weight: bold;
}}

.medium {{
    color: orange;
    font-weight: bold;
}}

.low {{
    color: blue;
    font-weight: bold;
}}

</style>

</head>

<body>

<h1>Threat Intelligence Dashboard</h1>

<p><strong>Generated:</strong> {timestamp}</p>

<h2>Summary</h2>

<ul>
<li>HIGH: {high}</li>
<li>MEDIUM: {medium}</li>
<li>LOW: {low}</li>
<li>Total IPs: {total}</li>
</ul>

<h2>Threat Feed</h2>

<table>

<tr>
<th>Timestamp</th>
<th>IP Address</th>
<th>Risk</th>
<th>Threat Score</th>
</tr>
"""

for row in csv_data:

    html += f"""
<tr>
<td>{row[0]}</td>
<td>{row[1]}</td>
<td class="{row[2].lower()}">{row[2]}</td>
<td>{row[3]}</td>
</tr>
"""

html += """
</table>

</body>

</html>
"""

with open(
    "threat-dashboard.html",
    "w"
) as file:

    file.write(html)

print("\n threat-report.txt generated")
print(" threat-report.csv generated")
print(" threat-dashboard.html generated")
