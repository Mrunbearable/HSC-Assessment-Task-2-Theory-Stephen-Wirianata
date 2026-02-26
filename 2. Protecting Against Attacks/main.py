from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encrypt a sensitive file
def encrypt_file(file_path):
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher_suite.encrypt(file_data)
    with open(file_path + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)
    print(f"File {file_path} encrypted successfully.")
# Decrypt the encrypted file
def decrypt_file(encrypted_file_path):
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    original_file_path = encrypted_file_path.replace('.enc', '')
    with open(original_file_path, 'wb') as file:
        file.write(decrypted_data)
    print(f"File {original_file_path} decrypted successfully.")

# Example usage
encrypt_file('2. Protecting Against Attacks\sensitive_data.txt')
decrypt_file('2. Protecting Against Attacks\sensitive_data.txt.enc')