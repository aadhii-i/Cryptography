def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


def ofb_encrypt(plaintext, key, iv):
    result = b""
    feedback = iv

    for i in range(0, len(plaintext), len(key)):
        feedback = xor_bytes(feedback, key)
        block = plaintext[i:i + len(key)]
        result += xor_bytes(block, feedback)

    return result


plaintext = input("Enter plaintext: ").encode()
key = input("Enter key (8 characters): ").encode()
iv = input("Enter IV (8 characters): ").encode()

if len(key) != 8 or len(iv) != 8:
    print("Key and IV must be exactly 8 characters.")
else:
    ciphertext = ofb_encrypt(plaintext, key, iv)

    print("Ciphertext:", ciphertext.hex())

    decrypted = ofb_encrypt(ciphertext, key, iv)
    print("Decrypted text:", decrypted.decode())