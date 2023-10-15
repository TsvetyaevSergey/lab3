from random import randint
import os


def encrypt(m, n):
    return (m * m) % n


def decrypt(c, p, q):
    a1 = pow(c, (p + 1) / 4) % p
    a2 = - pow(c, (p + 1) / 4) % p
    b1 = pow(c, (q + 1) / 4) % q
    b2 = - pow(c, (q + 1) / 4) % q

    p1 = china(a1, b1, p, q)
    p2 = china(a1, b2, p, q)
    p3 = china(a2, b1, p, q)
    p4 = china(a2, b2, p, q)
    return p1, p2, p3, p4


def china(a, b, p, q):
    M = p * q
    mp = M // p
    mq = M // q
    yp = pow(mp, -1, p)
    yq = pow(mq, -1, q)
    x = (a * mp * yp + b * mq * yq) % M
    return x


def gen_keys(m: int):
    p = 0
    q = 0
    while p * q < m:
        while not is_prime(p):
            k = randint(2, 5)
            p = 4 * k + 3
        while not is_prime(q) or p == q:
            k = randint(2, 5)
            q = 4 * k + 3
    return p, q


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

message = int(os.getenv("message"))
print(f"Start message = {message}")
p, q = gen_keys(message)
print(f"Keys = {p,q}")
enc = encrypt(message, p*q)
print(f"Encrypted message = {enc}")
print(f"Decrypted message = {decrypt(enc, p, q)}")
