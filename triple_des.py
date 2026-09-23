# Triple DES
# Name: Adhil Rahiman M
# Roll No: 2023BCS0187

from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad

print("Name: Adhil Rahiman M")
print("Roll No: 2023BCS0187")

plaintext = "Meet me after the toga party"

key = b"0123456789ABCDEF01234567"

cipher = DES3.new(key, DES3.MODE_ECB)

encrypted = cipher.encrypt(pad(plaintext.encode(), DES3.block_size))

decipher = DES3.new(key, DES3.MODE_ECB)
decrypted = unpad(
    decipher.decrypt(encrypted),
    DES3.block_size
).decode()

print("\nTriple DES Operation")
print("Plaintext :", plaintext)
print("Key       :", key.decode())
print("Encrypted :", encrypted.hex())
print("Decrypted :", decrypted)
