s = input()
letter = s[0]
number = int(s[1])
if ((letter == "A" or letter == "C" or letter == "E" or letter == "G") and number % 2 == 1) or ((letter == "B" or letter == "D" or letter == "F" or letter == "H") and number % 2 == 0):
    print("BLACK")
else:
    print("WHITE")
