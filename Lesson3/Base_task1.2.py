s = input()
count_upper = 0
count_lower = 0
for i in s:
    if 97 <= ord(i) <= 122:
        count_lower += 1
    elif 65 <= ord(i) <= 90:
        count_upper += 1
print(" The amount of upper case letters in the string is", count_upper)
print(" The amount of lower case letters in the string is", count_lower)
