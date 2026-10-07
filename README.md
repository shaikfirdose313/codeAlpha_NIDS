# CodeAlpha Network Intrusion Detection System (NIDS)

## Project Overview

This project is a basic Network Intrusion Detection System (NIDS) developed as part of the CodeAlpha Cyber Security Internship.

The system monitors network traffic and detects potentially unusual traffic patterns using predefined thresholds. When suspicious activity is detected, the system generates an alert.

## Objective

The main objectives of this project are:

* Monitor network traffic.
* Identify unusual network activity.
* Detect high packet activity from a single source IP.
* Generate alerts when predefined thresholds are exceeded.
* Understand the basic working principles of a Network Intrusion Detection System.

## Technologies Used

* Python
* Scapy
* GitHub
* Visual Studio Code

## Project Structure

```text
CodeAlpha_NIDS/
│
├── nids.py
├── rules.txt
├── requirements.txt
└── README.md
```

## How It Works

The NIDS captures network packets using Scapy and examines the source and destination IP addresses.

The program maintains a packet count for each source IP address. If the number of packets from a source exceeds the configured threshold within a specified time period, the system generates an alert.

### Detection Logic

* Time window: 10 seconds
* Packet threshold: 20 packets
* If a source IP sends more than 20 packets within the time window, an alert is generated.

## Installation

Install Python on your computer and then install the required Scapy library:

```bash
pip install scapy
```

You can also install the dependencies using:

```bash
pip install -r requirements.txt
```

## How to Run

Open the project folder in a terminal and run:

```bash
python nids.py
```

The program will start monitoring network traffic.

Press:

```text
Ctrl + C
```

to stop the program.

## Example Output

```text
Starting Network Intrusion Detection System...
Press Ctrl+C to stop.

Packet: 20.50.201.201 -> 10.235.189.213
Packet: 10.235.189.213 -> 20.50.201.201
Packet: 10.235.189.213 -> 20.50.201.201
Packet: 10.235.189.213 -> 20.50.201.201
Packet: 20.50.201.201 -> 10.235.189.213
Packet: 10.235.189.213 -> 10.235.189.104
Packet: 10.235.189.213 -> 10.235.189.104
Packet: 10.235.189.104 -> 10.235.189.213
Packet: 10.235.189.104 -> 10.235.189.213
Packet: 10.235.189.213 -> 2.20.1.188
Packet: 10.235.189.213 -> 20.50.201.201
```

## Detection Rules

The project uses simple educational detection rules:

1. Detect unusually high packet activity from a single source IP.
2. Monitor repeated network traffic patterns.
3. Generate an alert when the configured packet threshold is exceeded.

## Limitations

This is a basic educational NIDS and is not intended to replace professional intrusion detection systems.

It uses simple threshold-based detection and may not detect sophisticated attacks or advanced network threats.

## Ethical Use

This project is intended for cybersecurity education and authorized network monitoring only.

Only monitor network traffic on systems or networks where you have permission to do so. Do not use this project to monitor other people's private network traffic without authorization.

## Conclusion

This project demonstrates the basic concept of a Network Intrusion Detection System. It shows how network packets can be monitored, analyzed using simple rules, and used to generate alerts for potentially unusual activity.
