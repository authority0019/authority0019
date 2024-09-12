import socket

def get_all_ip_addresses():
    # Get all network interfaces
    interfaces = socket.if_nameindex()

    ip_addresses = set()

    for interface in interfaces:
        # Get the name of the network interface
        interface_name = interface[1]

        # Get the IPv4 and IPv6 addresses of the network interface
        ipv4_addresses = socket.getaddrinfo(interface_name, None, socket.AF_INET)
        ipv6_addresses = socket.getaddrinfo(interface_name, None, socket.AF_INET6)

        # Add IPv4 addresses
        for address in ipv4_addresses:
            ip_address = address[4][0]
            ip_addresses.add(ip_address)

        # Add IPv6 addresses
        for address in ipv6_addresses:
            ip_address = address[4][0]
            ip_addresses.add(ip_address)

    return ip_addresses

def main():
    all_ip_addresses = get_all_ip_addresses()
    if all_ip_addresses:
        print("All IP addresses of the device:")
        for ip_address in all_ip_addresses:
            print(ip_address)
    else:
        print("No IP addresses found for the device.")

if __name__ == "__main__":
    main()
