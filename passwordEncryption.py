from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

masterPassword = "Romulus"

def encryptPassword(password):
    salt = get_random_bytes(16)
    key = PBKDF2(masterPassword, salt, dkLen=32)
    cipher = AES.new(key, AES.MODE_CBC)
    
    cipherText = cipher.encrypt(pad(password.encode(), AES.block_size))
    
    return salt, cipher.iv + cipherText

    