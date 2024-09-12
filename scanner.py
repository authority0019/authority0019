import socket
from termcolor import colored

def scan(target, start_port, end_port):
    print(colored(f"[*] Starting scan for {target}...\n", "cyan"))
    open_ports = []

    try:
        for port in range(start_port, end_port + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)  # Connection timeout
                result = sock.connect_ex((target, port))
                if result == 0:
                    open_ports.append(port)
                    print(colored(f"[+] Port {port} is open at {target}.", "green"))
    except KeyboardInterrupt:
        print(colored("\n[!] Scan interrupted by user.", "yellow"))
        return
    except socket.gaierror:
        print(colored("[!] Target address could not be resolved. Please enter a valid IP address or hostname.", "red"))
        return
    except socket.error as e:
        print(colored(f"[!] Connection error: {e}", "red"))
        return

    if open_ports:
        print(colored("\n[+] Scan completed. Open ports:", "green"))
        for port in open_ports:
            print(colored(f"    - {port}", "green"))
    else:
        print(colored("\n[-] No open ports found during the scan.", "yellow"))

def main():
    print(colored("== Port Scanning Tool ==", "magenta"))
    target = input("[*] Enter the target IP address or hostname to scan: ")

    while True:
        try:
            start_port = int(input("[*] Enter the starting port for scanning (1-65535): "))
            if 1 <= start_port <= 65535:
                break
            else:
                print(colored("[!] Please enter a valid port number.", "red"))
        except ValueError:
            print(colored("[!] Please enter an integer.", "red"))

    while True:
        try:
            end_port = int(input("[*] Enter the ending port for scanning (1-65535): "))
            if 1 <= end_port <= 65535:
                break
            else:
                print(colored("[!] Please enter a valid port number.", "red"))
        except ValueError:
            print(colored("[!] Please enter an integer.", "red"))

    if start_port > end_port:
        start_port, end_port = end_port, start_port

    scan(target, start_port, end_port)

if __name__ == "__main__":
    main()
