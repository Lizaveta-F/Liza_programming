N = int(input())
for i in range(N):
    if 2**i <= N:
        print(2**i, end=" ")
