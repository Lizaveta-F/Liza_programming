from math import sqrt
a, b, c = float(input()), float(input()), float(input())
if a > 0 and b > 0 and c > 0:
    if a+b > c and b+c > a and c+a > b:
        half_per = (a+b+c)/2
        s = sqrt(half_per*(half_per-a)*(half_per-b)*(half_per-c))
        print("Площадь треугольника =", s)
    else:
        print("Данные введены некорректно")
else:
    print("Данные введены некорректно")
