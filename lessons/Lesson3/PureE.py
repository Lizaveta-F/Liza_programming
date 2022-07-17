from math import e
n = int(input())
if 0 <= n <= 25:
    print(round(e, n))
else:
    print("An inccorrect input data")
