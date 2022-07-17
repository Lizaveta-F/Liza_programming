N = int(input())
arr = list(map(int, input().split()))
count_days = 0
days = []
for i in arr:
    if i > 0:
        count_days += 1
    else:
        count_days = 0
    days.append(count_days)
days.sort()
print(days[-1])
