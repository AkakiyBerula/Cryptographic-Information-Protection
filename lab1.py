from math import ceil as ceil_length

    
def swap_cols(matrix, a, b):
    for k in range(0, len(matrix)):
        matrix[k][a], matrix[k][b] = matrix[k][b], matrix[k][a]

def splitter(string, cols, strs):
    matrix = []
    buf_string = string
    for a in range(strs):
        matrix.append(list(buf_string[0:cols]))
        buf_string = buf_string[cols:]
        if len(buf_string) < cols:
            buf_string = buf_string.ljust(cols, " ")
            
    return matrix

def encrypt(matrix, col_keys, row_keys):
    for i in range (1, len(col_keys)):
        temp = col_keys[i]
        j = i - 1
        while j >= 0 and temp < col_keys[j]:
            swap_cols(matrix, j + 1, j)
            col_keys[j + 1] = col_keys[j]
            j -= 1
        col_keys[j + 1] = temp
        
    for i in range(1, len(row_keys)):
        temp = row_keys[i]
        j = i - 1
        while j >= 0 and temp < row_keys[j]:
            matrix[j + 1], matrix[j] = matrix[j], matrix[j + 1]
            row_keys[j + 1] = row_keys[j]
            j -= 1
        row_keys[j + 1] = temp
        
    return matrix

def print_crypt(matrix, col_len, row_len):
    print("Зашифрований текст: ", end=" ")
    for i in range(0, col_len):
        for j in range(0, row_len):
            print(matrix[j][i], end="")
        print(" ", end="")
    print()
    
def print_matrix(matrix):
    print("Матриця:")
    for array in matrix:
        for i in array:
            print(i, end=" ")
        print()
        
def print_keys(col_key, row_key):
    print("Стовпцевий ключ:", end=" ")
    for i in col_key:
        print(i, end=" ")
    print("\nРядковий ключ:", end=" ")
    for i in row_key:
        print(i, end=" ")
    print()

   
input_data = input("Введіть рядок для шифрування: ").replace(' ', '').lower()
column_key = list(input("Введіть стовпцевий ключ: ").lower())
string_key = list(input("Введіть рядковий ключ: ").lower())

if len(column_key) * len(string_key) < len(input_data):
    print("Текст занадто довгий для введених ключів!!!")
elif len(input_data) <= 0 or len(column_key) <= 0 or len(column_key) <= 0:
    print("Відсутні деякі дані!!!")
else:
    string_key = string_key[:ceil_length(len(input_data) / len(column_key))]
    result = splitter(input_data, len(column_key), len(string_key))
    print_matrix(result)
    print_keys(column_key, string_key)
    
    encrypt(result, column_key, string_key)
    print("\nШифрування даних було проведено!!!\n")
    
    print_crypt(result, len(column_key), len(string_key))
    print_matrix(result)
    print_keys(column_key, string_key)

