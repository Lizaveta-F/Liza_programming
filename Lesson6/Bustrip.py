N = int(input())
arr = list(map(int, input().split()))
count_bridges = 0
crash_number = ""
for i in range(len(arr)):
    if arr[i] > 437:
        Flag = True
        count_bridges += 1
    else:
        crash_number = i+1
        break
if count_bridges == N:
    print("No crash")
else:
    print("Crash", crash_number)
