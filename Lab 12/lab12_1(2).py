def gcdex(a, b):
    x_0, x_1 = 1, 0
    y_0, y_1 = 0, 1
    d_0, d_1 = a, b
    while d_1 != 0:
        q = d_0 // d_1
        d_0, d_1 = d_1, d_0 - d_1 *q
        x_0, x_1 = x_1, x_0 - q * x_1
        y_0, y_1 = y_1, y_0 - q * y_1

    return d_0, x_0, y_0

def inverse_element(a, n):
    g, x, y = gcdex(a, n)
    if g == 1:
        return x % n
    else:
        raise ValueError("Оберненого елемента не існує! Числа не є взаємно прості!")
    
def add_points(p, q, a, p_field):
    if p[0] != q[0] or p[1] != q[1]:
        temp = inverse_element(q[0] - p[0], p_field)
        m = (q[1] - p[1]) * temp
    else:
        temp = inverse_element(2 * p[1], p_field)
        m = (3 * pow(p[0], 2) + a) * temp
    x_r = (pow(m, 2) - p[0] - q[0]) % p_field
    y_r = (m * (p[0] - x_r) - p[1]) % p_field

    return x_r, y_r

def multiply_point(base_point, scalar, a, p_field):
    result = base_point
    for bit in bin(scalar)[3:]:
        result = add_points(result, result, a, p_field)
        if bit == '1':
            result = add_points(result, base_point, a, p_field)

    return result

def find_order(base_point, a, p):
    order = 1
    result = base_point
    print(f"Точка {order} - {result}")
    while result[0] != base_point[0] or order == 1:
        order += 1
        result = multiply_point(base_point, order, a, p)
        print(f"Точка {order} - {result}")
    
    return order + 1


a = 1
b = 1
mod_p = 23
point = (17, 20)

if (point[1] ** 2) % mod_p == (point[0] ** 3 + a * point[0] + b) % mod_p:
    order = find_order(point, a, mod_p)
    print(f"Порядок n точки {point} еліптичної кривої (a: {a}, b: {b}, p: {mod_p}) дорівнює {order}")
else:
    print("Точка не належить еліптичній кривій!!!")





