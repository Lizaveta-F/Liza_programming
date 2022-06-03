from math import e
n = int(input())
if n == 0:
    print(3)
elif n > 24:
    print(e)
else:
    print(float(str(e)[:n+2]))
