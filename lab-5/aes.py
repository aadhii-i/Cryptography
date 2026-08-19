from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

key = get_random_bytes(16)
plaintext = b"Hello AES World!"

# AES requires 16-byte blocks, so pad manually
padding = 16 - len(plaintext) % 16
plaintext = plaintext + bytes([padding]) * padding

cipher = AES.new(key, AES.MODE_ECB)
encrypted = cipher.encrypt(plaintext)

cipher = AES.new(key, AES.MODE_ECB)
decrypted = cipher.decrypt(encrypted)

padding = decrypted[-1]
decrypted = decrypted[:-padding]

print("Plaintext :", decrypted.decode())
print("Key       :", base64.b64encode(key).decode())
print("Encrypted :", base64.b64encode(encrypted).decode())
print("Decrypted :", decrypted.decode())
