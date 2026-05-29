def analyze_logs():

    warning_count = 0
    error_count = 0

    with open("logs/sample-log.txt", "r") as file:

        lines = file.readlines()

        for line in lines:

            if "WARNING" in line:
                warning_count += 1

            elif "ERROR" in line:
                error_count += 1

    return warning_count, error_count
