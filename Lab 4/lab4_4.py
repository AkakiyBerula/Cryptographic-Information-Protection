

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

def phi(m):
    if m < 1:
        return ValueError("Не було введене натуральне число!!!")
    phi = m
    i = 2
    while i * i <= m:
        if m % i == 0:
            while m % i == 0:
                m //= i
            phi -= phi // i
        i += 1

    if m > 1:
        phi -= phi // m

    return phi

def inverse_element_2(a, n):
    phi_n = phi(n)

    d, x, y = gcdex(a, n)

    if d != 1:
        raise ValueError("Оберненого елемента не існує! Числа не є взаємно прості!")

    inverse = pow(a, phi_n - 1, n)
    return inverse


a = int(input("Введіть значення a: "))
n = int(input("Введіть значення n: "))

try:
    result = inverse_element_2(a, n)
    print(f"Мультиплікативний обернений елемент для {a} по модулю {n} дорівнює {result}")
except ValueError as e:
    print(e)