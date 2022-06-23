N = int(input())
a, b = 0, 1
i = 1
while a+b <= N:
    a, b = b, a+b
    i += 1
if N == b:
    print(1, i, sep='\n')
else:
    print(0)
