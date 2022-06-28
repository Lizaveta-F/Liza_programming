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

def generateAllBinaryStrings(n, lst, i):
    if i == n:
        print(lst)
        return lst
    lst[i] = '0'
    generateAllBinaryStrings(n, lst, i + 1)
    lst[i] = '1'
    generateAllBinaryStrings(n, lst, i + 1)
    # def generate(lst):
    #     yield from (lst)
n=int(input())
generateAllBinaryStrings(n, [0]*n, 0)


" не понимаю, что менять..."