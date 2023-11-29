import random

def is_prime_miller_rabin(n, k):
    if n <= 3 or n % 2 == 0 or k < 0:
        return None
    
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for i in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for j in range(r - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False

    return True

def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if is_prime_miller_rabin(num, 5):
            return num
        
def generate_generator(p):
    phi = p - 1
    while True:
        g = random.randint(2, p - 1)
        if pow(g, 2, p) != 1 and pow(g, phi // 2, p) != 1:
            return g


bits = 64
p = generate_prime(bits)
g = generate_generator(p)

a_private = random.randint(2, p - 2)
a_public = pow(g, a_private, p)

b_private = random.randint(2, p - 2)
b_public = pow(g, b_private, p)

shared_secret_alice = pow(b_public, a_private, p)
shared_secret_bob = pow(a_public, b_private, p)


print("Просте число p:", p)
print("Генератор g:", g)
print("Приватний ключ Аліси:", a_private)
print("Публічний ключ Аліси:", a_public)
print("Приватний ключ Боба:", b_private)
print("Публічний ключ Боба:", b_public)
print("Секрет Аліси:", shared_secret_alice)
print("Секрет Боба:", shared_secret_bob)
print("Ключ спільний? -", True if shared_secret_alice == shared_secret_bob else False)


