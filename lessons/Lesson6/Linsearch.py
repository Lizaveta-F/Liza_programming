N = int(input())
arr = list(map(int, input().split()))
X = int(input())
count = 0
for i in arr:
    if i == X:
        count += 1
print(count)
