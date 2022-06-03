s = input()
digitAmount = 0
upperAmount = 0
lowerAmount = 0
if len(s) <= 100:
    for i in range(len(s)):
        if 48 <= ord(s[i]) <= 57 or 65 <= ord(s[i]) <= 122:
            if 48 <= ord(s[i]) <= 57:
                digitAmount += 1
            elif 65 <= ord(s[i]) <= 90:
                upperAmount += 1
            else:
                lowerAmount += 1
if digitAmount >= 1 and upperAmount >= 1 and lowerAmount >= 1 and len(s) >= 12:
    print("YES")
else:
    print("NO")
