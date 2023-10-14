from math import ceil as ceil_length


class TranspositionCipher:
    is_encrypted = False
    
    def __init__ (self, string, col_key, row_key):
        self.col_key = col_key
        self.row_key = row_key[:ceil_length(len(input_data) / self.count_col_len())]
        self.matrix = self.splitter(string, self.count_col_len(), self.count_row_len())
    
    def count_col_len(self):
        return len(self.col_key)
    
    def count_row_len(self):
        return len(self.row_key)
    
    def swap_cols(self, a, b):
        for k in range(0, self.count_row_len()):
            self.matrix[k][a], self.matrix[k][b] = self.matrix[k][b], self.matrix[k][a]
            
    def splitter(self, string, cols, rows):
        matrix = []
        buf_string = string
        for a in range(rows):
            matrix.append(list(buf_string[0:cols]))
            buf_string = buf_string[cols:]
            if len(buf_string) < cols:
                buf_string = buf_string.ljust(cols, " ")
            
        return matrix

    @staticmethod
    def encrypt(data):
        for i in range (1, data.count_col_len()):
            temp = data.col_key[i]
            j = i - 1
            while j >= 0 and temp < data.col_key[j]:
                data.swap_cols(j + 1, j)
                data.col_key[j + 1] = data.col_key[j]
                j -= 1
            data.col_key[j + 1] = temp
        
        for i in range(1, data.count_row_len()):
            temp = data.row_key[i]
            j = i - 1
            while j >= 0 and temp < data.row_key[j]:
                data.matrix[j + 1], data.matrix[j] = data.matrix[j], data.matrix[j + 1]
                data.row_key[j + 1] = data.row_key[j]
                j -= 1
            data.row_key[j + 1] = temp
        
        data.is_encrypted = True

    def print_crypt(self):
        print("Зашифрований текст: ", end=" ")
        for i in range(0, self.count_col_len()):
            for j in range(0, self.count_row_len()):
                print(self.matrix[j][i], end="")
            print(" ", end="")
        print()
        
    def print_matrix(self):
        print("Матриця:")
        for array in self.matrix:
            for i in array:
                print(i, end=" ")
            print()
        
    def print_keys(self):
        print("Стовпцевий ключ:", end=" ")
        for i in self.col_key:
            print(i, end=" ")
        print("\nРядковий ключ:", end=" ")
        for i in self.row_key:
            print(i, end=" ")
        print()
        

input_data = input("Введіть рядок для шифрування: ").replace(' ', '').lower()
column_key = list(input("Введіть стовпцевий ключ: ").replace(' ', '').lower())
string_key = list(input("Введіть рядковий ключ: ").replace(' ', '').lower())

if len(column_key) * len(string_key) < len(input_data):
    print("Текст занадто довгий для введених ключів!!!")
elif len(input_data) <= 0 or len(column_key) <= 0 or len(column_key) <= 0:
    print("Відсутні деякі дані!!!")
else:
    result = TranspositionCipher(input_data, column_key, string_key)
    result.print_matrix()
    result.print_keys()
    
    TranspositionCipher.encrypt(result)
    print("\nШифрування даних було проведено!!!\n")
    
    result.print_crypt()
    result.print_matrix()
    result.print_keys()

