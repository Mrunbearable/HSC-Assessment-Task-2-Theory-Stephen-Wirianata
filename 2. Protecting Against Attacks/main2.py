from cryptography.fernet import Fernet
import os
import hmac
import hashlib

key = Fernet.generate_key()
cipher_suite = Fernet(key)


def constant_time_compare(val1, val2):
    return hmac.compare_digest(val1, val2)

STORED_PASSWORD_HASH = hashlib.sha256(b"stephen").hexdigest()

def authenticate():
    user_input = input("Enter password to decrypt: ").encode()
    user_hash = hashlib.sha256(user_input).hexdigest()
    if constant_time_compare(user_hash, STORED_PASSWORD_HASH):
        print("Authentication successful.")
        return True
    else:
        print("Authentication failed.")
        return False

def encrypt_file(file_path):
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher_suite.encrypt(file_data)
    with open(file_path + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)
    print(f"File {file_path} encrypted successfully.")


def decrypt_file(encrypted_file_path):
    if not authenticate():
        print("Access denied. Cannot decrypt file.")
        return
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    original_file_path = encrypted_file_path.replace('.enc', '')
    with open(original_file_path, 'wb') as file:
        file.write(decrypted_data)
    print(f"File {original_file_path} decrypted successfully.")

encrypt_file('2. Protecting Against Attacks\sensitive_data.txt')
decrypt_file('2. Protecting Against Attacks\sensitive_data.txt.enc')
# The password is "stephen"