N = int(input())
wages = []
for _ in range(N):
    wages.append(list(map(int, input().split())))
wages.sort()
print("For mother-in-law:", *wages[0])
print("For myself:", *wages[-1])
