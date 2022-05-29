from math import sqrt
a, b, c = float(input()), float(input()), float(input())
a > 0, b > 0, c > 0
wrong = "Данные введены некорректно"
if a:
    if b:
        if c:
            if a+b > c:
                if b+c > a:
                    if c+a > b:
                        half_per = (a+b+c)/2
                        s = sqrt(half_per*(half_per-a) *
                                 (half_per-b)*(half_per-c))
                        print("Площадь треугольника =", s)
                    else:
                        print(wrong)
                else:
                    print(wrong)
            else:
                print(wrong)
        else:
            print(wrong)
    else:
        print(wrong)
else:
    print(wrong)
