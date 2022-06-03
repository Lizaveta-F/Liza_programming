n = int(input())
n_in_s = str(n)
if 0 < n <= 10**30:
    Count0 = n_in_s.count('0')
    print("The amount of 0 is", Count0)
else:
    print("The input data is incorrect")
