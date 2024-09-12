import random
import string

def generate_fake_link(protocol='http://', domain='', top_level_domain='com', path='', query_params=None):
    if not domain:
        domain = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10)))
    if not path:
        path = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(5, 15)))
    
    fake_link = f"{protocol}{domain}.{top_level_domain}/{path}"

    if query_params:
        fake_link += '?' + '&'.join([f"{param}={value}" for param, value in query_params.items()])
    
    return fake_link

def main():
    print("Fake Link Generator\n")

    protocol = input("Choose protocol (http or https, default: http): ").lower() or 'http'
    domain = input("Enter domain (default: random): ")
    top_level_domain = input("Enter top-level domain (default: com): ").lower() or 'com'
    path = input("Enter path (default: random): ")

    num_links = int(input("\nHow many fake links do you want to generate?: "))

    query_params_choice = input("\nDo you want to add query parameters? (Y/N): ").strip().lower()
    query_params = {}
    if query_params_choice == 'y':
        num_params = int(input("How many query parameters do you want to add?: "))
        for _ in range(num_params):
            param_name = input("Enter parameter name: ")
            param_value = input("Enter parameter value: ")
            query_params[param_name] = param_value

    print("\nFake Links:")
    for i in range(num_links):
        fake_link = generate_fake_link(protocol, domain, top_level_domain, path, query_params)
        print(fake_link)

if __name__ == "__main__":
    main()
