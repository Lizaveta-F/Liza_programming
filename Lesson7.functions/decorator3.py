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
n = int(input())
def generateAllBinaryStrings(n,i):
    lst=['0']*n
    lst[i]='0'
    yield from lst
    generateAllBinaryStrings(n, i + 1)
    lst[i] = '1'
    generateAllBinaryStrings(n,  i + 1)

print([lst for lst in generateAllBinaryStrings(n,0)])

