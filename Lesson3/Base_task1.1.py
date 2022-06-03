s = input()
count_upper = 0
count_lower = 0
for i in range(len(s)):
    if 65 <= ord(s[i]) <= 90:
        count_upper += 1
    if 97 <= ord(s[i]) <= 122:
        count_lower += 1
print("The amount of lowercase is", count_lower)
print("The amount of uppercase is", count_upper)
