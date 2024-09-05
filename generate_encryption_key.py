import os
from cryptography.fernet import Fernet

def generate_and_save_key(file_name="encryption_key.txt"):
    key = Fernet.generate_key()
    with open(file_name, "wb") as key_file:
        key_file.write(key)
    return file_name

if __name__ == "__main__":
    print("Generating and saving encryption key...")
    file_name = generate_and_save_key()
    print(f"Encryption key saved to {os.getcwd()}/{os.path.basename(file_name)}")
