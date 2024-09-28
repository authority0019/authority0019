from scapy.all import *

def send_custom_packet(dst_ip):
    packet = IP(dst=dst_ip) / ICMP()
    send(packet)
    print(f"Packet sent to {dst_ip}")

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    send_custom_packet(target_ip)