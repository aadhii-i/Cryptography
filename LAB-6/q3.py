from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad

# Fixed key and IV
key = b"123456789012345678901234"
iv = b"12345678"

# Fixed plaintext
plaintext = b"HELLO TRIPLE DES"

# Encryption
cipher = DES3.new(key, DES3.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(plaintext, DES3.block_size))

print("Plaintext :", plaintext.decode())
print("Ciphertext:", ciphertext.hex())

# Decryption
cipher = DES3.new(key, DES3.MODE_CBC, iv)
decrypted = unpad(cipher.decrypt(ciphertext), DES3.block_size)

print("Decrypted :", decrypted.decode())