N = int(input())
max_ = 0
arr = list(map(int, input().split()))
for i in range(1, N-1):
    summa = arr[i]+arr[i-1]+arr[i+1]
    if summa >= max_:
        max_ = summa
print(max_)
