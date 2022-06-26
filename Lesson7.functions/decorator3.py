# Реализовать функцию-генератор, генерирующую бинарные строки рекурсивно 
# (всё, как и в задании на рекурсию, но функция-генератор). Используйте yield from
# # так делать не надо =))))
# for el in binary_strings(2):
#     print(el)
# '''
# всё те же
# 00
# 01
# 10
# 11
# '''

def generateAllBinaryStrings(n, arr, i):
    if i == n:
        print("".join(arr))
        return arr
    lst=[0]*n
    while i <n:
        lst[i]='0'
        yield from lst
        generateAllBinaryStrings(n, arr, i + 1)
        arr[i] = '1'
        generateAllBinaryStrings(n, arr, i + 1)


n = int(input())

generateAllBinaryStrings(n, [0]*n, 0)