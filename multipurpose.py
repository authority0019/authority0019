import os
import subprocess

def change_mac(interface, new_mac):
    print(f"Changing MAC address of {interface} to {new_mac}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    print("MAC address changed successfully.")

def change_ip(interface, new_ip):
    print(f"Changing IP address of {interface} to {new_ip}")
    subprocess.call(["ifconfig", interface, new_ip])
    print("IP address changed successfully.")

def display_menu():
    print("\n--- Network Configuration Menu ---")
    print("1. Change MAC Address")
    print("2. Change IP Address")
    print("3. Exit")

def main():
    while True:
        display_menu()
        choice = input("Select an option (1-3): ")

        if choice == '1':
            interface = input("Enter the network interface (e.g., eth0, wlan0): ")
            new_mac = input("Enter the new MAC address (format XX:XX:XX:XX:XX:XX): ")
            change_mac(interface, new_mac)

        elif choice == '2':
            interface = input("Enter the network interface (e.g., eth0, wlan0): ")
            new_ip = input("Enter the new IP address (format XXX.XXX.XXX.XXX): ")
            change_ip(interface, new_ip)

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()