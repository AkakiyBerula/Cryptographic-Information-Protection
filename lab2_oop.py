
class VigenereCipher:
    
    alphabet = list("абвгдеєжзиіїйклмнопрстуфхцчшщьюя")
    is_encrypted = False
    
    @staticmethod
    def count_len(text):
        return len(text)
    
    @staticmethod
    def create_key(key_text, len_text, len_key):
        return key_text * (len_text // len_key) + key_text[:len_text % len_key]
        
    def __init__(self, text, key_text):
        self.text = text
        self.key = self.create_key(key_text, self.count_len(text), self.count_len(key_text))
        self.is_encrypted = False

    def encryption(self):
        crypted_text = ""
        i = 0
        for d in self.text:
            index_d = self.alphabet.index(d)
            index_key = self.alphabet.index(self.key[i])
            index_c = (index_d + index_key) % 32
            crypted_text += self.alphabet[index_c]
            i += 1
        self.text = crypted_text
        self.is_encrypted = True
    
    def decryption(self):
        decrypted_text = ""
        i = 0
        for c in self.text:
            index_c = self.alphabet.index(c)
            index_key = self.alphabet.index(self.key[i])
            index_d = (index_c - index_key + 32) % 32
            decrypted_text += self.alphabet[index_d]
            i += 1
        self.text = decrypted_text
        self.is_encrypted = False
        
    def compare_text(self, text):
        return text == self.text
        
    def print_text(self):
        if self.is_encrypted:
            print("Зашифрований текст: ")
        else:
            print("Розшифрований текст: ")
        print(self.text)
        
    def print_data(self):
        print(f"Текст = {self.text}")
        print(f"Ключ = {self.key}")
        

text = input("Введіть текст: ").replace(" ", "").lower()
key = input("Введіть ключ: ").replace(" ", "").lower()

if len(text) == 0 or len(key) == 0:
    print("Відсутні деякі дані!!!")
else:
    result = VigenereCipher(text, key)

    result.print_data()

    result.encryption()
    result.print_text()

    result.decryption()
    result.print_text()
    
    print(f"Виконання: {result.compare_text(text)}")
