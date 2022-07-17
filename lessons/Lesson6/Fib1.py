f1 = f2 = 1
n = int(input("Number of Fib-element ")) - 2
while n > 0:
    f1, f2 = f2, f1 + f2
    n -= 1
print("The fib number is", f2)
