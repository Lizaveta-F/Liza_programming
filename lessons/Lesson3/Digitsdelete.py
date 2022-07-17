s = input()
count = 0
if len(s) <= 100:
    for i in range(len(s)):
        if 33 <= ord(s[i]) <= 127:
            count += 1
if count == len(s):
    if '4' in s or '7' in s:
        s_new = s.replace('4', "")
        s_new1 = s_new.replace('7', "")
        print(s_new1)
    else:
        print("There is no 4 or 7 in the input data")
else:
    print("The input data is incorrect")
