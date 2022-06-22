s, p = map(int, input().split())
d = s**2+4*(-p)
y = int((-s+d*(0.5))/(-2))
x = s-y
if x < y:
    print(x, y)
else:
    print(y, x)
