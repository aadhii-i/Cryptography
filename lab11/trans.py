def encrypt(text, key):
    text = text.replace(" ", "").upper()
    n = len(key)

    rows = [text[i:i+n] for i in range(0, len(text), n)]
    res = ""

    for col in sorted(range(n), key=lambda i: (key[i], i)):
        for row in rows:
            if col < len(row):
                res += row[col]

    return res

def decrypt(text, key):
    n = len(key)
    rows = (len(text) + n - 1) // n
    extra = len(text) % n

    if extra == 0:
        extra = n

    order = sorted(range(n), key=lambda i: (key[i], i))
    cols = {}
    pos = 0

    for col in order:
        length = rows if col < extra else rows - 1
        cols[col] = text[pos:pos+length]
        pos += length

    res = ""
    for r in range(rows):
        for c in range(n):
            if r < len(cols[c]):
                res += cols[c][r]

    return res

text = input("Enter plaintext: ").upper()
key1 = input("Enter first key: ").upper()

if not key1.isalpha():
    print("Invalid key")
else:
    single = encrypt(text, key1)
    print("Single transposition:", single)
    print("Single decrypted:", decrypt(single, key1))

    key2 = input("Enter second key: ").upper()

    if not key2.isalpha():
        print("Invalid key")
    else:
        double = encrypt(single, key2)
        print("Double transposition:", double)
        print("Double decrypted:", decrypt(decrypt(double, key2), key1))
