N = int(input())
a = []
arr = list(map(int, input().split()))
X = int(input())
for i in range(N-1):
    diff = abs(X - arr[i])
    a.append(diff)
print(max(a))
