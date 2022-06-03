n = int(input())
count = 0
n_in_s = str(n)
length1 = len(n_in_s)
if 0 < n <= 10**30:
    length2 = len(n_in_s.replace('0', ""))
    dif = length1-length2
    print("The amount of 0 is", dif)
else:
    print("The input data is incorrect")
