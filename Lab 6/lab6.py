S_BOX = [
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
]

INV_S_BOX = [
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D
]


def key_expansion(key):
    round_constants = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]
    round_keys = [key[i:i + 4] for i in range(0, len(key), 4)]
    for i in range(4, 44):
        temp = round_keys[i - 1][:]
        if i % 4 == 0:
            temp = [temp[1], temp[2], temp[3], temp[0]]
            temp = [S_BOX[b] for b in temp]
            temp[0] ^= round_constants[i // 4 - 1]
        round_keys.append([a ^ b for a, b in zip(round_keys[i - 4], temp)])

    return round_keys


def add_round_key(state, round_key):
    for i in range(4):
        for j in range(4):
            state[i][j] ^= round_key[i][j]
    return state


def sub_bytes(state):
    for i in range(4):
        for j in range(4):
            state[i][j] = S_BOX[state[i][j]]
    return state


def shift_rows(state):
    for i in range(1, 4):
        row_to_shift = [state[j][i] for j in range(len(state))]
        shifted_row = row_to_shift[i:] + row_to_shift[:i]
        for j in range(len(state)):
            state[j][i] = shifted_row[j]
    return state


def mix_columns(state):
    for i in range(4):
        s0 = state[i][0]
        s1 = state[i][1]
        s2 = state[i][2]
        s3 = state[i][3]
        state[i][0] = mul02(s0) ^ mul03(s1) ^ s2 ^ s3
        state[i][1] = s0 ^ mul02(s1) ^ mul03(s2) ^ s3
        state[i][2] = s0 ^ s1 ^ mul02(s2) ^ mul03(s3)
        state[i][3] = mul03(s0) ^ s1 ^ s2 ^ mul02(s3)
    return state


def mul02(byte):
    if byte & 0x80:
        result = (byte << 1) ^ 0x1B
    else:
        result = byte << 1
    return result & 0xFF


def mul03(byte):
    return mul02(byte) ^ byte


def encrypt(plain_text, key):
    state = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            state[i][j] = plain_text[i * 4 + j]

    print("Starting bytestring:")
    check_func(state)

    key_list= [[0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            key_list[i][j] = key[i * 4 + j]

    print("Starting keybytestring:")
    check_func(key_list)

    round_keys = key_expansion(key)
    state = add_round_key(state, round_keys[0:4])

    for round_num in range(1, 10):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, round_keys[round_num * 4 : (round_num + 1) * 4])

        print(f"After Round {round_num}:")
        check_func(state)

    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, round_keys[40:])

    print("After Round 10 (Final):")
    check_func(state)

    cipher_text = [state[i][j] for i in range(4) for j in range(4)]
    return bytes(cipher_text)


def inv_shift_rows(state):
    for i in range(1, 4):
        row_to_shift = [state[j][i] for j in range(len(state))]
        shifted_row = row_to_shift[-i:] + row_to_shift[:-i]
        for j in range(len(state)):
            state[j][i] = shifted_row[j]
    return state


def inv_sub_bytes(state):
    for i in range(4):
        for j in range(4):
            state[i][j] = INV_S_BOX[state[i][j]]
    return state


def inv_mix_columns(state):
    for i in range(4):
        s0 = state[i][0]
        s1 = state[i][1]
        s2 = state[i][2]
        s3 = state[i][3]
        state[i][0] = mul0e(s0) ^ mul0b(s1) ^ mul0d(s2) ^ mul09(s3)
        state[i][1] = mul09(s0) ^ mul0e(s1) ^ mul0b(s2) ^ mul0d(s3)
        state[i][2] = mul0d(s0) ^ mul09(s1) ^ mul0e(s2) ^ mul0b(s3)
        state[i][3] = mul0b(s0) ^ mul0d(s1) ^ mul09(s2) ^ mul0e(s3)
    return state


def mul09(byte):
    result = byte
    result = mul02(byte)
    result = mul02(result)
    result = mul02(result)
    result = result ^ byte
    return result


def mul0b(byte):
    result = mul02(byte)
    result = mul02(result)
    result = result ^ byte
    result = mul02(result)
    result = result ^ byte
    return result


def mul0d(byte):
    result = mul02(byte)
    result = result ^ byte
    result = mul02(result)
    result = mul02(result)
    result = result ^ byte
    return result


def mul0e(byte):
    result = mul02(byte)
    result = result ^ byte
    result = mul02(result)
    result = result ^ byte
    result = mul02(result)
    return result


def decrypt(cipher_text, key):
    state = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            state[i][j] = cipher_text[i * 4 + j]

    print("Starting bytestring:")
    check_func(state)

    round_keys = key_expansion(key)
    state = add_round_key(state, round_keys[40:])

    for round_num in range(9, 0, -1):
        state = inv_shift_rows(state)
        state = inv_sub_bytes(state)
        state = add_round_key(state, round_keys[round_num * 4 : (round_num + 1) * 4])
        state = inv_mix_columns(state)

        print(f"After Round {round_num + 1}:")
        check_func(state)

    state = inv_shift_rows(state)
    state = inv_sub_bytes(state)
    state = add_round_key(state, round_keys[0:4])

    print("After Round 1 (Final):")
    check_func(state)

    plain_text = [state[i][j] for i in range(4) for j in range(4)]
    return bytes(plain_text)

def check_func(state):
    for row in state:
        print(''.join([hex(num)[2:].zfill(2) for num in row]), end=' ')
    print()


message = input("Введіть текстове повідомлення (16 символів): ").encode('utf-8')
key = input("Введіть ключ (16 символів): ")

if len(key) != 16:
    print("Ключ має бути довжиною 8 символів!!!")
elif len(message) != 16:
    print("Текстове повідомлення має бути довжиною 8 символів!!!")
else:
    key = bytes(key, 'utf-8')
    crypted_text = encrypt(message, key)
    print("Зашифрований текст:", crypted_text.hex())  # Convert bytes to hexadecimal string
    decrypted_text = decrypt(crypted_text, key)
    print("Розшифрований текст:", decrypted_text.decode('utf-8'))
