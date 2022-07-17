s = input()
if "A" in s or "C" in s or "E" in s or "G" in s:
    if "1" in s or "3" in s or "5" in s or "7" in s:
        print("BLACK")
    else:
        print("WHITE")
elif "B" in s or "D" in s or "F" in s or "H" in s:
    if "2" in s or "4" in s or "6" in s or "8" in s:
        print("BLACK")
    else:
        print("WHITE")
