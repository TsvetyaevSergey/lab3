from random import randint
import os


def encrypt(m, n):
    c = []
    for char in m:
        c.append((ord(char) * ord(char)) % n)
    return c


def decrypt(c, p, q):
    decrypted_text = []
    for char in c:
        a1 = pow(char, (p + 1) / 4) % p
        a2 = - pow(char, (p + 1) / 4) % p
        b1 = pow(char, (q + 1) / 4) % q
        b2 = - pow(char, (q + 1) / 4) % q

        p1 = china(a1, b1, p, q)
        p2 = china(a1, b2, p, q)
        p3 = china(a2, b1, p, q)
        p4 = china(a2, b2, p, q)
        decrypted_text.append([chr(int(p1)), chr(int(p2)), chr(int(p3)), chr(int(p4))])
    return decrypted_text


def china(a, b, p, q):
    M = p * q
    mp = M // p
    mq = M // q
    yp = pow(mp, -1, p)
    yq = pow(mq, -1, q)
    x = (a * mp * yp + b * mq * yq) % M
    return x


def gen_keys():
    p = 0
    q = 0
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


message = os.getenv("message")
print(f"Start message = {message}")
p, q = gen_keys()
print(f"Keys = {p,q}")
enc = encrypt(message, p*q)
print(f"Encrypted message = {enc}")
dec = decrypt(enc, p, q)
print(f"Decrypted message = ")
for i in dec:
    print(i)
