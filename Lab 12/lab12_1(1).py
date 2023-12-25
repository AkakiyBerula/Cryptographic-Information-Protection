def find_points_on_curve(a, b, p):
    points = []
    for x in range(p):
        y_square = (pow(x, 3) + a * x + b) % p
        for y in range(0, p):
            if pow(y, 2, p) == y_square:
                points.append((x, y))

    return points

a = 1
b = 1
p = 23
curve_points = find_points_on_curve(a, b, p)
print("Усі точки еліптичної кривої y^2 = (x^3 + x + 1)(mod 23):")
for point in curve_points:
    print(point, end = ", ")





