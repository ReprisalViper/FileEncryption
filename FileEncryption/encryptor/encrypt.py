import os
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def save_key(key, filename):
    with open(filename, 'wb') as file:
        file.write(key)

def encrypt_file(filepath, key):
    if not os.path.isfile(filepath):
        print(f"❌ File not found: {filepath}")
        return

    fernet = Fernet(key)
    with open(filepath, 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)
    with open(filepath + ".enc", 'wb') as file:
        file.write(encrypted)

    print(f"✅ File encrypted: {filepath}.enc")

if __name__ == "__main__":
    file_path = input("Enter full path of the file to encrypt: ").strip()
    key = generate_key()
    save_key(key, 'secret.key')
    encrypt_file(file_path, key)
