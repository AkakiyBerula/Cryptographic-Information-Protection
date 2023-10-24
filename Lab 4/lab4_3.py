

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

m = int(input("Введіть число m для визначення значення функції Ейлера: "))
try:
    result = phi(m)
    print(f"Значення функції Ейлера для числа {m} = {result}")
except ValueError as e:
    print(e)