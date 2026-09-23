# Diffie-Hellman Key Exchange
# Name: Adhil Rahiman M
# Roll No: 2023BCS0187

print("=" * 50)
print("DIFFIE-HELLMAN KEY EXCHANGE")
print("Name    :", "Adhil Rahiman M")
print("Roll No :", "2023BCS0187")
print("=" * 50)

p = int(input("Enter prime number (p): "))
g = int(input("Enter primitive root (g): "))

a = int(input("Enter private key of Alice: "))
b = int(input("Enter private key of Bob: "))

A = pow(g, a, p)
B = pow(g, b, p)

key_alice = pow(B, a, p)
key_bob = pow(A, b, p)

print("\nPublic key of Alice:", A)
print("Public key of Bob  :", B)

print("Shared key of Alice:", key_alice)
print("Shared key of Bob  :", key_bob)

if key_alice == key_bob:
    print("\nKey exchange successful!")
else:
    print("\nKey exchange failed!")
