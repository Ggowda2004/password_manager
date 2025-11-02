# encryption.py
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_password(key, password):
    cipher = Fernet(key)
    return cipher.encrypt(password.encode())

def decrypt_password(key, encrypted_password):
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_password).decode()
