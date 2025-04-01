from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64
import re

KEY = b''  # 8 字节密钥
IV = bytes.fromhex("") 

def des_encrypt(plaintext: str) -> str:
    cipher = DES.new(KEY, DES.MODE_CBC, IV)
    padded_text = pad(plaintext.encode(), DES.block_size)
    encrypted = cipher.encrypt(padded_text)
    return base64.b64encode(encrypted).decode()

def des_decrypt(ciphertext: str) -> str:
    ciphertext = re.sub(r"\s+", "", ciphertext)
    cipher = DES.new(KEY, DES.MODE_CBC, IV)
    decrypted = cipher.decrypt(base64.b64decode(ciphertext))
    return unpad(decrypted, DES.block_size).decode()