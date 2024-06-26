import sys
from scapy.all import *

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        payload = packet[Raw].load if Raw in packet else None
        
        print(f"Source IP: {src_ip}, Destination IP: {dst_ip}, Protocol: {proto}")
        if payload:
            print("Payload:", payload.hex())

def main(interface):
    try:
        print(f"Sniffing on interface {interface}...")
        sniff(iface=interface, prn=packet_callback, store=0)
    except KeyboardInterrupt:
        print("Exiting...")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sniffer.py <interface>")
        sys.exit(1)
    interface = sys.argv[1]
    main(interface)
