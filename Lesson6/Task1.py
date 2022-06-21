# Выведите n-ое число Фибоначчи, используя только временные переменные, циклические операторы
# и условные операторы. n - вводится.
n = int(input())-2
fib1 = 1
fibn = 1
while n > 0:
    fib1, fibn = fibn, fib1+fibn
    n -= 1
print("The value of n-fibonacci:", fibn)

# # or
# fib1 = fibn = 1
# n = int(input())
# for i in range(2, n):
#     fib1, fibn = fibn, fib1 + fibn
# print("The value of n-fibonacci:", fibn)
