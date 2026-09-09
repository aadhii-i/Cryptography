import math


p = int(input("Enter first prime number: "))
q = int(input("Enter second prime number: "))

n = p * q
phi = (p - 1) * (q - 1)

e = int(input("Enter public key e: "))

if math.gcd(e, phi) != 1:
    print("Invalid e. It must be relatively prime to phi.")
else:
    d = pow(e, -1, phi)

    print("\nn =", n)
    print("phi =", phi)
    print("Public Key  =", (e, n))
    print("Private Key =", (d, n))

    message = int(input("Enter message (number < n): "))

    if message >= n:
        print("Message must be smaller than n.")
    else:
        ciphertext = pow(message, e, n)
        decrypted = pow(ciphertext, d, n)

        print("Encrypted message:", ciphertext)
        print("Decrypted message:", decrypted)