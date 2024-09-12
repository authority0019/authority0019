import requests
import socket
import whois
import json

def ip_info(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        print("[*] IP Information:")
        print("    IP Address:", data["query"])
        print("    City:", data["city"])
        print("    Country:", data["country"])
        print("    ISP:", data["isp"])
        print("    Organization:", data["org"])
    except Exception as e:
        print("[-] An error occurred while fetching IP information:", e)

def domain_info(domain):
    try:
        domain_info = whois.whois(domain)
        print("[*] Domain Information:")
        print("    Domain Name:", domain)
        print("    Registrar:", domain_info.registrar)
        print("    Creation Date:", domain_info.creation_date)
        print("    Expiration Date:", domain_info.expiration_date)
        print("    Name Servers:", domain_info.name_servers)
    except Exception as e:
        print("[-] An error occurred while fetching domain information:", e)

def main():
    target = input("[*] Enter IP address or Domain name: ")

    try:
        ip = socket.gethostbyname(target)
        print("[*] Target:", target)
        print("[*] IP Address:", ip)
        ip_info(ip)
        domain_info(target)
    except socket.gaierror:
        print("[-] Could not resolve hostname.")

if __name__ == "__main__":
    main()
