# Hill Cipher
# Name: Adhil Rahiman M
# Roll No: 2023BCS0187

import math

print("=" * 50)
print("HILL CIPHER")
print("Name    :", "Adhil Rahiman M")
print("Roll No :", "2023BCS0187")
print("=" * 50)

print("\nEnter 2x2 key matrix:")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))

det = (a * d - b * c) % 26

if math.gcd(det, 26) != 1:
    print("\nInvalid key matrix!")
    print("Determinant must be relatively prime to 26.")
    exit()

plaintext = input("\nEnter plaintext: ").upper()
plaintext = plaintext.replace(" ", "")

if len(plaintext) % 2 != 0:
    plaintext += "X"

ciphertext = ""

for i in range(0, len(plaintext), 2):

    x1 = ord(plaintext[i]) - ord('A')
    x2 = ord(plaintext[i + 1]) - ord('A')

    y1 = (a * x1 + b * x2) % 26
    y2 = (c * x1 + d * x2) % 26

    ciphertext += chr(y1 + ord('A'))
    ciphertext += chr(y2 + ord('A'))

print("\nKey Matrix:")
print("[", a, b, "]")
print("[", c, d, "]")

print("\nPlaintext :", plaintext)
print("Ciphertext:", ciphertext)
