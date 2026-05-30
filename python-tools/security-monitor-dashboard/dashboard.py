from modules.log_analyzer import analyze_logs
from modules.login_detector import detect_suspicious_logins
from modules.packet_sniffer import capture_packet

print("================================")
print(" SECURITY MONITORING DASHBOARD ")
print("================================")

# Log Analysis
warnings, errors = analyze_logs()

print("\nLog Analysis Results")
print("--------------------")
print(f"Warnings Detected: {warnings}")
print(f"Errors Detected: {errors}")

# Login Analysis
print("\nLogin Activity")
print("--------------")

failed_attempts = detect_suspicious_logins()

for ip, count in failed_attempts.items():

    print(f"{ip} -> Failed Attempts: {count}")

    if count >= 3:
        print(f"⚠️ ALERT: Possible brute-force attack from {ip}")

# Network Monitoring
print("\nNetwork Monitoring")
print("------------------")

packet = capture_packet()

if packet:

    print(f"Source IP: {packet['src']}")
    print(f"Destination IP: {packet['dst']}")
    print(f"Protocol: {packet['proto']}")

print("\nDashboard Loaded Successfully")
