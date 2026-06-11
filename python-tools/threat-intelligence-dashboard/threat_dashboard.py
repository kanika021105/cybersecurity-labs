import json
import csv
from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

high = 0
medium = 0
low = 0

report = []
csv_data = []

print("\n===== THREAT INTELLIGENCE DASHBOARD =====\n")

# Load Threat Feed
with open("threats.json", "r") as file:

    threats = json.load(file)

# Risk Filter
risk_filter = input(
    "Filter by risk (HIGH/MEDIUM/LOW/ALL): "
).upper()

filtered_threats = []

for threat in threats:

    if risk_filter == "ALL":

        filtered_threats.append(threat)

    elif threat["risk"] == risk_filter:

        filtered_threats.append(threat)

# Search Feature
search_ip = input(
    "Search IP (or press Enter to skip): "
).strip()

if search_ip:

    found = False

    print("\n===== SEARCH RESULTS =====\n")

    for threat in threats:

        if threat["ip"] == search_ip:

            print(
                f"IP: {threat['ip']} | Risk: {threat['risk']}"
            )

            found = True

    if not found:

        print("IP not found in threat feed")

print("\n===== THREAT REPORT =====\n")

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

total = high + medium + low

print("\n===== DASHBOARD SUMMARY =====\n")

print(f"HIGH: {high}")
print(f"MEDIUM: {medium}")
print(f"LOW: {low}")

print(f"\nTotal IPs Analysed: {total}")

# Risk Analytics
print("\n===== RISK ANALYTICS =====\n")

if total > 0:

    high_percent = (high / total) * 100
    medium_percent = (medium / total) * 100
    low_percent = (low / total) * 100

else:

    high_percent = 0
    medium_percent = 0
    low_percent = 0

print(f"HIGH Risk: {high_percent:.1f}%")
print(f"MEDIUM Risk: {medium_percent:.1f}%")
print(f"LOW Risk: {low_percent:.1f}%")

# Environment Risk Rating
if high >= 2:

    overall_risk = "CRITICAL"

elif high >= 1:

    overall_risk = "HIGH"

elif medium >= 2:

    overall_risk = "MEDIUM"

else:

    overall_risk = "LOW"

print(
    f"\nOverall Environment Risk: {overall_risk}"
)

# Top Threats
print("\n===== TOP THREATS =====\n")

for threat in filtered_threats:

    if threat["risk"] == "HIGH":

        print(threat["ip"])

# Generate Text Report
with open(
    "threat-report.txt",
    "w"
) as file:

    file.writelines(report)

# Generate CSV Report
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

# Generate HTML Dashboard
html = f"""
<!DOCTYPE html>
<html>

<head>

<title>Threat Intelligence Dashboard</title>

<style>

body {{
    font-family: Arial, sans-serif;
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

<h2>Risk Analytics</h2>

<ul>
<li>HIGH Risk: {high_percent:.1f}%</li>
<li>MEDIUM Risk: {medium_percent:.1f}%</li>
<li>LOW Risk: {low_percent:.1f}%</li>
<li>Environment Risk: {overall_risk}</li>
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
