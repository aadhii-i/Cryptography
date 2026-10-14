# ECC algorithm with user input

p = int(input("Enter prime p: "))
a = int(input("Enter a: "))
b = int(input("Enter b: "))

def inv(n, p):
    return pow(n % p, -1, p)

def add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and (y1 + y2) % p == 0:
        return None

    if P == Q:
        m = ((3 * x1 * x1 + a) * inv(2 * y1, p)) % p
    else:
        m = ((y2 - y1) * inv(x2 - x1, p)) % p

    x3 = (m * m - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p

    return (x3, y3)

def mul(k, P):
    R = None
    while k > 0:
        if k % 2:
            R = add(R, P)
        P = add(P, P)
        k //= 2
    return R

Gx = int(input("Enter base point Gx: "))
Gy = int(input("Enter base point Gy: "))
G = (Gx, Gy)

d = int(input("Enter private key d: "))
k = int(input("Enter encryption key k: "))

M = (int(input("Enter message point Mx: ")),
     int(input("Enter message point My: ")))

# Key generation
Q = mul(d, G)
print("Public key Q:", Q)

# Encryption: C1 = kG, C2 = M + kQ
C1 = mul(k, G)
C2 = add(M, mul(k, Q))

print("Encrypted C1:", C1)
print("Encrypted C2:", C2)

# Decryption: M = C2 - dC1
D = mul(d, C1)

if D is None:
    recovered = C2
else:
    recovered = add(C2, (D[0], (-D[1]) % p))

print("Decrypted message point:", recovered)
