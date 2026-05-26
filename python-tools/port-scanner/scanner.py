import socket

target = input("Enter target IP or website: ")

print(f"\nScanning target: {target}\n")

ports = [21, 22, 23, 25, 53, 80, 443]

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")

    s.close()
