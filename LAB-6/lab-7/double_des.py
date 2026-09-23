# Double DES
# Name: Adhil Rahiman M
# Roll No: 2023BCS0187

print("=" * 50)
print("DOUBLE DES")
print("Name    :", "Adhil Rahiman M")
print("Roll No :", "2023BCS0187")
print("=" * 50)


def des_encrypt(text, key):
    result = ""

    for i in range(len(text)):
        result += chr(ord(text[i]) ^ ord(key[i % len(key)]))

    return result


def des_decrypt(text, key):
    return des_encrypt(text, key)


plaintext = input("\nEnter plaintext: ")
key1 = input("Enter first key: ")
key2 = input("Enter second key: ")

# First encryption
step1 = des_encrypt(plaintext, key1)

# Second encryption
ciphertext = des_encrypt(step1, key2)

print("\nPlaintext       :", plaintext)
print("First Key       :", key1)
print("Second Key      :", key2)

print("After DES-1     :", repr(step1))
print("Ciphertext      :", repr(ciphertext))

# Decryption
step2 = des_decrypt(ciphertext, key2)
decrypted = des_decrypt(step2, key1)

print("\nDecryption:")
print("After DES-2     :", repr(step2))
print("Decrypted Text  :", decrypted)
