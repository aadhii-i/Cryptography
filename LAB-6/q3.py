from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad


plaintext = input("Enter plaintext: ")
key = input("Enter key (16 or 24 characters): ")
iv = input("Enter IV (8 characters): ")

key = key.encode()
iv = iv.encode()
plaintext = plaintext.encode()

if len(key) not in [16, 24]:
    print("Key must be 16 or 24 characters.")

elif len(iv) != 8:
    print("IV must be exactly 8 characters.")

else:
    # Encryption
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext, DES3.block_size))

    print("Encrypted text:", ciphertext.hex())

    # Decryption
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(ciphertext), DES3.block_size)

    print("Decrypted text:", decrypted.decode())