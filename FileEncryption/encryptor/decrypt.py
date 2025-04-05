import os
from cryptography.fernet import Fernet

def load_key(key_path):
    if not os.path.isfile(key_path):
        print(f"❌ Key file not found: {key_path}")
        return None
    with open(key_path, 'rb') as file:
        return file.read()

def decrypt_file(file_path, key):
    if not os.path.isfile(file_path):
        print(f"❌ Encrypted file not found: {file_path}")
        return

    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        encrypted = file.read()

    try:
        decrypted = fernet.decrypt(encrypted)
    except Exception as e:
        print(f"❌ Decryption failed: {e}")
        return

    output_path = file_path.replace(".enc", ".dec")
    with open(output_path, 'wb') as file:
        file.write(decrypted)
    print(f"✅ File decrypted: {output_path}")

if __name__ == "__main__":
    file_path = input("Enter full path of the encrypted file (e.g. /path/to/file.enc): ").strip()
    key_path = input("Enter full path to the key file (e.g. /path/to/secret.key): ").strip()
    key = load_key(key_path)
    if key:
        decrypt_file(file_path, key)
