

def gcdex(a, b):
    x_0, x_1 = 1, 0
    y_0, y_1 = 0, 1
    d_0, d_1 = a, b

    print("{a_0} \t {a_1} \t {x_0} \t {x_1} \t {y_0} \t {y_1}")
    print(f"{d_0:5d} \t {d_1:5d} \t {x_0:5d} \t {x_1:5d} \t {y_0:5d} \t {y_1:5d}")

    while d_1 != 0:
        q = d_0 // d_1
        d_0, d_1 = d_1, d_0 - d_1 *q
        x_0, x_1 = x_1, x_0 - q * x_1
        y_0, y_1 = y_1, y_0 - q * y_1
        print(f"{d_0:5d} \t {d_1:5d} \t {x_0:5d} \t {x_1:5d} \t {y_0:5d} \t {y_1:5d}")

    print()
    return d_0, x_0, y_0

a = int(input("Введіть значення a: "))
b = int(input("Введіть значення b: "))
d, x, y = gcdex(a, b)

print(f"НСД({a}, {b}) = {d}")
print(f"Коефіцієнти Безу: x = {x}, y = {y}")
print(f"{a} * {x} + {b} * {y} = {d}")