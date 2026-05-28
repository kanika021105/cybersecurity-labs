## Objective
To capture and analyze live network packets using Python and Scapy.

---

# Observations

## TCP Traffic

Observed:
- Source and destination IP addresses
- Protocol number 6 (TCP)

This represented normal web communication.

---

## UDP Traffic

Observed:
- Protocol number 17 (UDP)
- Destination IP 224.0.0.251

This is associated with multicast DNS (mDNS) used for local network discovery.

---

# Key Learning

This project helped in understanding:
- packet capture
- source and destination IPs
- TCP and UDP protocols
- live traffic monitoring
- Python packet analysis using Scapy

 ---
 
## Screenshot

![Packet Sniffer Output](../../screenshots/packet-sniffer-output.png)
