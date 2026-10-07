from scapy.all import sniff, IP
from collections import defaultdict
import time

packet_count = defaultdict(int)
start_time = time.time()

THRESHOLD = 20
TIME_WINDOW = 10


def packet_callback(packet):
    global start_time

    if IP not in packet:
        return

    source_ip = packet[IP].src
    destination_ip = packet[IP].dst

    packet_count[source_ip] += 1

    elapsed = time.time() - start_time

    if elapsed >= TIME_WINDOW:
        for ip, count in packet_count.items():
            if count > THRESHOLD:
                print("\n[ALERT] High traffic detected")
                print("Source IP      :", ip)
                print("Packet Count   :", count)

        packet_count.clear()
        start_time = time.time()

    print(
        "Packet:",
        source_ip,
        "->",
        destination_ip
    )


print("Starting Network Intrusion Detection System...")
print("Press Ctrl+C to stop.")

sniff(prn=packet_callback, store=False)