from cryptography.fernet import Fernet

def key_generation():
    key_new = Fernet.generate_key()
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key_new)
    return key_new

def file_encrypt(filename,key):
    fernet = Fernet(key)
    with open(filename, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(filename, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def file_decrypt(filename,key):
    fernet = Fernet(key)
    with open(filename, 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(filename, 'wb') as dec_file:
        dec_file.write(decrypted)

