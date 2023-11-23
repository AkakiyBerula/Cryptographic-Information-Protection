import random

def gcdex(a, b):
    x_0, x_1 = 1, 0
    y_0, y_1 = 0, 1
    d_0, d_1 = a, b

    while d_1 != 0:
        q = d_0 // d_1
        d_0, d_1 = d_1, d_0 - d_1 * q
        x_0, x_1 = x_1, x_0 - q * x_1
        y_0, y_1 = y_1, y_0 - q * y_1

    return d_0, x_0, y_0

def inverse_element(a, n):
    g, x, y = gcdex(a, n)
    if g == 1:
        return x % n
    else:
        raise ValueError("Оберненого елемента не існує! Числа не є взаємно прості!")

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

def generate_keypair(bits):
    p = generate_prime(bits)
    q = generate_prime(bits)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi - 1)
    while gcdex(e, phi)[0] != 1:
        e = random.randint(2, phi - 1)

    d = inverse_element(e, phi)

    return ((e, n), (d, n))

def encrypt(message, public_key):
    e, n = public_key
    return pow(message, e, n)


def decrypt(ciphertext, private_key):
    d, n = private_key
    return pow(ciphertext, d, n)

# Приклад використання
bits = 512
public_key, private_key = generate_keypair(bits)

try:
    message = int(input("Введіть повідомлення: "))

    encrypted_message = encrypt(message, public_key)
    print(f"Зашифроване повідомлення: {encrypted_message}")

    decrypted_message = decrypt(encrypted_message, private_key)
    print(f"Розшифроване повідомлення: {decrypted_message}")
    
except ValueError:
    print("Введене значення не є цілим числом.")




