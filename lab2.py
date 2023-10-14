alphabet = "абвгдеєжзиіїйклмнопрстуфхцчшщьюя"
alphabet_list = list(alphabet)

def encryption(decrypted_text, key):
    crypted_text = ""
    i = 0
    for d in decrypted_text:
        index_d = alphabet_list.index(d)
        index_key = alphabet_list.index(key[i])
        index_c = (index_d + index_key) % 32
        crypted_text += alphabet_list[index_c]
        i += 1
    return crypted_text
    
def decryption(crypted_text, key):
    decrypted_text = ""
    i = 0
    for c in crypted_text:
        index_c = alphabet_list.index(c)
        index_key = alphabet_list.index(key[i])
        index_d = (index_c - index_key + 32) % 32
        decrypted_text += alphabet_list[index_d]
        i += 1
    return decrypted_text

text = input("Введіть текст: ").replace(" ", "").lower()
key = input("Введіть ключ: ").replace(" ", "").lower()

if len(text) == 0 or len(key) == 0:
    print("Відсутні деякі дані!!!")
else:
    len_text = len(text)
    len_key = len(key)
    create_key_for_text = key * (len_text // len_key) + key[:len_text % len_key]

    print(f"Текст = {text}")
    print(f"Ключ = {create_key_for_text}")

    encrypted_text = encryption(text, create_key_for_text)
    print(f"Зашифрований = {encrypted_text}")

    decrypted_text = decryption(encrypted_text, create_key_for_text)
    print(f"Розшифрований = {decrypted_text}")

    print(f"Виконання: {text == decrypted_text}")

