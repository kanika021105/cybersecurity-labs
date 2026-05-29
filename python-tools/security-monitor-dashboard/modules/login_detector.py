def detect_suspicious_logins():

    failed_attempts = {}

    with open("logs/login-log.txt", "r") as file:

        lines = file.readlines()

        for line in lines:

            parts = line.strip().split()

            ip = parts[0]
            status = parts[1]

            if status == "FAILED":

                if ip not in failed_attempts:
                    failed_attempts[ip] = 1
                else:
                    failed_attempts[ip] += 1

    return failed_attempts
