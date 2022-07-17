s = input()
count = 0
if 1 <= len(s) <= 100:
    for i in range(len(s)):
        if 65 <= ord(s[i]) <= 122:
            count += 1
if count == len(s):
    s_new = '#'.join(s)
    print(s_new)
else:
    print("The input data is incorrect")
