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

def text_to_numbers(text):
    return [ord(char) for char in text]

def numbers_to_text(numbers):
    return ''.join([chr(num) for num in numbers])

def generate_keypair(bits):
    p = generate_prime(bits)
    g = generate_generator(p)
    x = random.randint(1, p - 1)
    y = pow(g, x, p)

    public_key = (p, g, y)
    private_key = (p, x)

    return public_key, private_key

def encrypt(message, public_key):
    p, g, y = public_key
    k = random.randint(1, p - 2)
    plaintext_numbers = text_to_numbers(message)
    encrypted_message = []
    for num in plaintext_numbers:
        k = random.randint(1, p - 1)
        c1 = pow(g, k, p)
        c2 = (pow(y, k, p) * num) % p
        encrypted_message.append((c1, c2))

    return encrypted_message

def decrypt(encrypted_message, private_key):
    p, x = private_key
    decrypted_numbers = []
    for c1, c2 in encrypted_message:
        s = pow(c1, x, p)
        num = (c2 * pow(s, -1, p)) % p
        decrypted_numbers.append(num)

    decrypted_message = numbers_to_text(decrypted_numbers)
    return decrypted_message


bits = 64
public_key, private_key = generate_keypair(bits)

message = input("Введіть повідомлення: ")

ciphertext = encrypt(message, public_key)
print("\nЗашифроване повідомлення:", ciphertext)

decrypted_message = decrypt(ciphertext, private_key)
print("\nРозшифроване повідомлення:", decrypted_message)
