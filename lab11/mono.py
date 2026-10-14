def encrypt(text, key):
    res = ""
    for ch in text.upper():
        if ch.isalpha():
            res += key[ord(ch) - ord('A')]
        else:
            res += ch
    return res

def decrypt(text, key):
    res = ""
    for ch in text.upper():
        if ch.isalpha():
            res += chr(key.index(ch) + ord('A'))
        else:
            res += ch
    return res

key = input("Enter 26-letter key: ").upper()
text = input("Enter plaintext: ")

if len(key) != 26 or not key.isalpha() or len(set(key)) != 26:
    print("Invalid key")
else:
    enc = encrypt(text, key)
    print("Ciphertext:", enc)
    print("Decrypted text:", decrypt(enc, key))
