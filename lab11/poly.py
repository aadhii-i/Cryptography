def encrypt(text, key):
    res = ""
    j = 0
    key = key.upper()

    for ch in text.upper():
        if ch.isalpha():
            k = ord(key[j % len(key)]) - ord('A')
            c = (ord(ch) - ord('A') + k) % 26
            res += chr(c + ord('A'))
            j += 1
        else:
            res += ch

    return res

def decrypt(text, key):
    res = ""
    j = 0
    key = key.upper()

    for ch in text.upper():
        if ch.isalpha():
            k = ord(key[j % len(key)]) - ord('A')
            c = (ord(ch) - ord('A') - k) % 26
            res += chr(c + ord('A'))
            j += 1
        else:
            res += ch

    return res

key = input("Enter key: ").upper()
text = input("Enter plaintext: ")

if not key.isalpha():
    print("Invalid key")
else:
    enc = encrypt(text, key)
    print("Ciphertext:", enc)
    print("Decrypted text:", decrypt(enc, key))
