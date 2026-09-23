# AES and DES Encryption/Decryption
# Name: Adhil Rahiman M
# Roll No: 2023BCS0187

from Crypto.Cipher import AES, DES
from Crypto.Util.Padding import pad, unpad

print("Name: Adhil Rahiman M")
print("Roll No: 2023BCS0187")

plaintext = "Meet me after the toga party"

print("\nOriginal Plaintext:")
print(plaintext)

# ---------------- AES ----------------
aes_key = b"0123456789ABCDEF"

aes_cipher = AES.new(aes_key, AES.MODE_ECB)
aes_encrypted = aes_cipher.encrypt(
    pad(plaintext.encode(), AES.block_size)
)

aes_decipher = AES.new(aes_key, AES.MODE_ECB)
aes_decrypted = unpad(
    aes_decipher.decrypt(aes_encrypted),
    AES.block_size
).decode()

print("\n--- AES ---")
print("Key       :", aes_key.decode())
print("Encrypted :", aes_encrypted.hex())
print("Decrypted :", aes_decrypted)

# ---------------- DES ----------------
des_key = b"12345678"

des_cipher = DES.new(des_key, DES.MODE_ECB)
des_encrypted = des_cipher.encrypt(
    pad(plaintext.encode(), DES.block_size)
)

des_decipher = DES.new(des_key, DES.MODE_ECB)
des_decrypted = unpad(
    des_decipher.decrypt(des_encrypted),
    DES.block_size
).decode()

print("\n--- DES ---")
print("Key       :", des_key.decode())
print("Encrypted :", des_encrypted.hex())
print("Decrypted :", des_decrypted)
