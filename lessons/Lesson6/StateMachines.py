k = int(input())
lst1 = []
for i in range(k):
    n, m = map(int, input().split())
    d = 19 * m + (n + 239) * (n + 366) / 2
    lst1.append(d)
print(*lst1, sep="\n")
