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


message = input("Введіть текст для хешування: ").encode("UTF-8")
hashed_message = sha1(message).hex()
print(f'Хеш повідомлення: {hashed_message}')



