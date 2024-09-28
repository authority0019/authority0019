def xor_encrypt_decrypt(data, key):
    return ''.join(chr(ord(c) ^ ord(key)) for c in data)

if __name__ == "__main__":
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    key = input("Enter a single character key: ")
    
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode selected.")
        exit()
    
    filename = input("Enter the filename: ")
    
    with open(filename, 'r') as file:
        data = file.read()
    
    if mode == 'encrypt':
        processed_data = xor_encrypt_decrypt(data, key)
        with open(f"{filename}.enc", 'w') as file:
            file.write(processed_data)
        print(f"File encrypted as {filename}.enc")
    
    elif mode == 'decrypt':
        processed_data = xor_encrypt_decrypt(data, key)
        with open(f"{filename}.dec", 'w') as file:
            file.write(processed_data)
        print(f"File decrypted as {filename}.dec")