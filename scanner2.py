import os

def scan_network(network):
    print(f"Scanning network: {network}")
    os.system(f"ping -c 1 {network}.*")

if __name__ == "__main__":
    network_prefix = input("Enter the network prefix (e.g., 192.168.1): ")
    for i in range(1, 255):
        scan_network(network_prefix + "." + str(i))