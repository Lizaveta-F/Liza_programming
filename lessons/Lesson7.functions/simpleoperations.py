n = int(input())
a = list(map(int, input().split()))
m = int(input())
k = []
for i in range(m):
    i = input()
    k.append(i)

numbers = k[0][4:].split()
l = int(numbers[0])
r = int(numbers[1])
def rsq(l, r):
    summa = 0
    for i in a[l-1:r]:
        summa += int(i)
    print(summa)


numbers1 = k[1][7:].split()
l = int(numbers1[0])
r = int(numbers1[1])
x = numbers1[2]
def update(l, r, x):
    for i in range(len(a[l-1:r])):
        a[i] = x
    print(a)


numbers2 = k[2][4:].split()
l = int(numbers2[0])
r = int(numbers2[1])
def rmq(l, r):
    min_ = min(a[l-1:r])
    print(min_)


numbers3 = k[3][4:].split()
l = int(numbers3[0])
r = int(numbers3[1])
x = int(numbers3[2])
def add(l, r, x):
    for i in range(len(a[l-1:r])):
        a[i] = int(a[i])+x
    print(a)


numbers4 = k[4][4:].split()
y = int(numbers4[0])
def get(y):
    for i in range(1, len(a)+1):
        if i == y:
            print(a[i-1])


rsq(l, r)
update(l, r, x)
rmq(l, r)
add(l, r, x)
get(y)
