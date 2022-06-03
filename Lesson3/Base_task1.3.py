s = input()
summa_lower = 0
summa_upper = 0
for c in s:
    if ord(c) <= 122 and c.isalpha():
        if c == c.lower():
            summa_lower += 1
        elif c == c.upper():
            summa_upper += 1
print("The amount of upper case letters in the string is", summa_upper)
print("The amount of lower case letters in the string is", summa_lower)
