import random

def is_prime_miller_rabin(n, k):
    if n <= 3 or n % 2 == 0 or k < 0:
        return None
    
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for i in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for j in range(r - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False

    return True

def count_probability(k):
    return 1 - 0.5 ** k

# Приклад використання:
n = int(input("Введіть непарне число більше трьох для перевірки: "))
k = int(input("Введіть кільіксть раундів (додатнє число): "))

try:
    is_prime = is_prime_miller_rabin(n, k)

    if is_prime is True:
        print(f"{n} можливо просте за тестом Міллера-Рабіна.")
        print(f"Ймовірність простоти: {count_probability(k)}")
    elif is_prime is False:
        print(f"{n} складене за тестом Міллера-Рабіна.")
    else:
        print("Неправильно введені вхідні дані!!!")
except ValueError:
    print("Невірно введені дані!!!")