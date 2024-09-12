import requests

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("[+] Website is reachable:", url)
        else:
            print("[-] Website is unreachable:", url)
    except requests.ConnectionError:
        print("[-] Connection Error:", url)

websites = input("[*] Enter websites to check (split them by ,): ")

if ',' in websites:
    print("[*] Checking multiple websites")
    for site in websites.split(','):
        check_website(site.strip())
else:
    check_website(websites.strip())
