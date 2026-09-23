# ECC - Elliptic Curve Cryptography
# Name: Adhil Rahiman M
# Roll No: 2023BCS0187

p = 17
a = 2
b = 2

O = None

def inverse_mod(k, p):
    return pow(k % p, -1, p)

def point_add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and (y1 + y2) % p == 0:
        return None

    if P != Q:
        m = ((y2 - y1) * inverse_mod(x2 - x1, p)) % p
    else:
        if y1 == 0:
            return None
        m = ((3 * x1 * x1 + a) * inverse_mod(2 * y1, p)) % p

    x3 = (m * m - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p

    return (x3, y3)

def scalar_mult(k, P):
    R = None
    while k > 0:
        if k & 1:
            R = point_add(R, P)
        P = point_add(P, P)
        k >>= 1
    return R

G = (5, 1)

private_key = 3
public_key = scalar_mult(private_key, G)

print("Name: Adhil Rahiman M")
print("Roll No: 2023BCS0187")
print("\nECC Algorithm")
print("Elliptic Curve: y^2 = x^3 + 2x + 2 mod 17")
print("Base Point G:", G)
print("Private Key:", private_key)
print("Public Key:", public_key)

k = 2
R = scalar_mult(k, G)
S = scalar_mult(k, public_key)

print("\nEphemeral Key:", k)
print("R = kG:", R)
print("Shared Secret:", S)
