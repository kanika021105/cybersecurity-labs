import re

password = input("Enter your password: ")

strength = 0


if len(password) >= 8:
    strength += 1
else:
    print(" Password should be at least 8 characters long")

# Uppercase check
if re.search(r"[A-Z]", password):
    strength += 1
else:
    print(" Add at least one uppercase letter")


if re.search(r"[a-z]", password):
    strength += 1
else:
    print(" Add at least one lowercase letter")


if re.search(r"[0-9]", password):
    strength += 1
else:
    print(" Add at least one number")


if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    strength += 1
else:
    print(" Add at least one special character")


print("\n--- Password Strength Result ---")

if strength == 5:
    print(" Strong Password")

elif strength >= 3:
    print(" Medium Password")

else:
    print(" Weak Password")
