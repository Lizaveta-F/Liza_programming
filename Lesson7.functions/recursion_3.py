# Реализовать функцию binary_strings, принимающую на вход натуральное число n.
# Данная функция должна рекурсивно генерировать все бинарные строки длины n.
# Бинарная строка - строка, состоящая из 0 и 1.
# binary_strings(3)

# '''
# 000
# 001
# 010
# 011
# 100
# 101
# 110
# 111
# '''

def binary_strings(n, arr, i):
    if i == n:
        print("".join(arr))
        return arr
    arr[i] = '0'
    binary_strings(n, arr, i + 1)
    arr[i] = '1'
    binary_strings(n, arr, i + 1)


n = int(input())

binary_strings(n, [0]*n, 0)
