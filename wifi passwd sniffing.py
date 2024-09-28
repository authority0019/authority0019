from scapy.all import *

def packet_handler(packet):
    if packet.haslayer(Dot11):
        ssid = packet[Dot11].info.decode('utf-8', errors='ignore')
        signal_strength = packet[Dot11].dBm_AntSignal
        print(f"SSID: {ssid}, Signal Strength: {signal_strength} dBm")

if __name__ == "__main__":
    print("Starting Wi-Fi packet sniffer...")
    sniff(iface="wlan0", prn=packet_handler, store=0)

#install scapy before using, do pip install scapy