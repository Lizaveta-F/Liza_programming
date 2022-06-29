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


def getbin(n, s=['']):
    if n > 0:
        return [
            *getbin(n - 1, [i + '0' for i in s]),
            *getbin(n - 1, [j + '1' for j in s])]
    return s


def binary_strings(n, s=['']):
    yield from getbin(n, s=[''])


bin = binary_strings(3, s=[""])
print(next(bin))
print(next(bin))
print(next(bin))
