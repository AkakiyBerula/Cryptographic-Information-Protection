import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    if gcd(a, m) != 1:
        return None
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def generate_key(n):
    a = 0
    while True:
        a = random.randint(1, n - 1)
        if gcd(a, n) == 1:
            break

    s = random.randint(0, n - 1)
    return a, s

def affine_encrypt(text, a, b, alphabet):
    m = len(alphabet)
    ciphertext = ""
    for char in text:
        if char in alphabet:
            char_index = alphabet.index(char)
            encrypted_char = alphabet[(a * char_index + b) % m]
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext

def affine_decrypt(ciphertext, a, b, alphabet):
    m = len(alphabet)
    plaintext = ""
    a_inv = mod_inverse(a, m)
    for char in ciphertext:
        if char in alphabet:
            char_index = alphabet.index(char)
            decrypted_char = alphabet[(a_inv * (char_index - b)) % m]
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext


alphabet = "abcdefghijklmnopqrstuvwxyz"
a, b = generate_key(len(alphabet))
text = input("Введіть рядок тексту для проведення операції (латиною): \n").lower()
encrypted_text = affine_encrypt(text, a, b, alphabet)
decrypted_text = affine_decrypt(encrypted_text, a, b, alphabet)

print("Текст:", text)
print("Зашифрований текст:", encrypted_text)
print("Розшифрований текст:", decrypted_text)








