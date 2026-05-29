from modules.log_analyzer import analyze_logs

print("================================")
print(" SECURITY MONITORING DASHBOARD ")
print("================================")

warnings, errors = analyze_logs()

print("\nLog Analysis Results")
print("--------------------")
print(f"Warnings Detected: {warnings}")
print(f"Errors Detected: {errors}")

print("\nDashboard Loaded Successfully")
