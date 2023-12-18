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

def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def pack_words(words):
    return b''.join([value.to_bytes(4, 'big') for value in words])

def sha1(message):
    original_length = len(message)
    message += b'\x80'
    message += b'\x00' * ((56 - (original_length + 1) % 64) % 64)
    message += (original_length * 8).to_bytes(8, 'big')

    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    for i in range(0, len(message), 64):
        chunk = message[i:i + 64]
        words = [int.from_bytes(chunk[j:j + 4], 'big') for j in range(0, 64, 4)]
        for j in range(16, 80):
            words.append(left_rotate(words[j - 3] ^ words[j - 8] ^ words[j - 14] ^ words[j - 16], 1))

        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        for j in range(80):
            if j < 20:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif j < 40:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif j < 60:
                f = (b & c) | (b & d) | (c & d) 
                k = 0x8F1BBCDC
            elif j <= 80:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = left_rotate(a, 5) + f + e + k + words[j] & 0xFFFFFFFF
            e = d 
            d = c
            c = left_rotate(b, 30) 
            b = a
            a = temp

        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF

    return b''.join([value.to_bytes(4, 'big') for value in [h0, h1, h2, h3, h4]])

def elgamal_sign(message, p, g, x):
    while True:
        k = random.randint(1, p - 1)
        if is_prime_miller_rabin(k, 5):
            break

    r = pow(g, k, p)
    h = int.from_bytes(sha1(message), 'big')
    k_inverse = pow(k, -1, p - 1)
    s = (k_inverse * (h - x * r)) % (p - 1)

    return r, s

def elgamal_verify(message, signature, p, g, y):
    r, s = signature
    if not (1 < r < p - 1) or not (0 < s < p - 1):
        return False
    
    h = int.from_bytes(sha1(message), 'big')
    v1 = (pow(y, r, p) * pow(r, s, p)) % p
    v2 = pow(g, h, p)

    return v1 == v2


(p, g, y), (_, x) = generate_keypair(256)

message_to_sign = input("Введіть рядок для цифрового підпису: ").encode("UTF-8")
signature = elgamal_sign(message_to_sign, p, g, x)
is_valid = elgamal_verify(message_to_sign, signature, p, g, y)

print(f"Підпис: {signature}")
print(f"Чи є підпис дійсним: {is_valid}")

