N = int(input())
max_digit = 0
arr = list(map(int, input().split()))
L, R = int(input()), int(input())
arr1 = arr[L-1:R]
for j in range(N):
    for i in range(len(arr1)):
        if arr1[i] >= max_digit:
            max_digit = arr1[i]
            ind = j
print(max_digit, ind)
