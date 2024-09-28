import subprocess
import string
import random
import re
import argparse

def get_random_mac_address():
    """Generates a random MAC address in the format xx:xx:xx:xx:xx:xx."""
    return ":".join(random.choice(string.hexdigits) * 2 for _ in range(6))

def get_current_mac_address(interface):
    """Gets the current MAC address of the specified network interface."""
    output = subprocess.check_output(["ifconfig", interface])
    mac_address_match = re.search(r"hwaddr\s(\S+)", output.decode())
    if mac_address_match:
        return mac_address_match.group(1)
    else:
        raise ValueError(f"Could not find MAC address for interface {interface}")

def change_mac_address(interface, new_mac_address):
    """Changes the MAC address of the specified network interface."""
    try:
        subprocess.check_call(["sudo", "ifconfig", interface, "hwaddr", new_mac_address])
    except subprocess.CalledProcessError as e:
        print(f"Error changing MAC address: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python Mac Changer on Linux")
    parser.add_argument("interface", help="The network interface name on Linux")
    parser.add_argument("-r", "--random", action="store_true", help="Whether to generate a random MAC address")
    parser.add_argument("-m", "--mac", help="The new MAC you want to change to")
    args = parser.parse_args()

    iface = args.interface
    if args.random:
        new_mac_address = get_random_mac_address()
    elif args.mac:
        new_mac_address = args.mac
    else:
        parser.error("You must specify either -r or -m.")

    old_mac_address = get_current_mac_address(iface)
    print("[*] Old MAC address:", old_mac_address)

    change_mac_address(iface, new_mac_address)

    new_mac_address = get_current_mac_address(iface)
    print("[+] New MAC address:", new_mac_address)