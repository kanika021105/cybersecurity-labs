### Security Monitoring Dashboard

Developed a Python-based cybersecurity monitoring dashboard integrating log analysis, suspicious login detection, and network packet monitoring.
Implemented alert classification for security events and created a modular architecture using Python and Scapy for network traffic analysis.

# Security Monitoring Dashboard v1.0

## Features
- Log analysis
- Failed login detection
- Brute-force attack alerts
- Packet monitoring
- Alert summary panel

## Technologies
- Python
- Scapy

## Status
Version 1.0 completed

# Security Monitoring Dashboard Architecture

          +----------------+
          | dashboard.py   |
          +-------+--------+
                  |
        -------------------
        |        |        |
        v        v        v

+------------+ +------------+ +---------------+
| Log        | | Login      | | Packet        |
| Analyzer   | | Detector   | | Sniffer       |
+------------+ +------------+ +---------------+

        |
        v

+-------------------+
| Alert Summary     |
+-------------------+
