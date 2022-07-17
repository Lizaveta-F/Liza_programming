# Реализовать функцию print_backward, принимающую на вход список.
# Данная функция должна рекурсивно выводить в обратном порядке элементы этого списка в stdout
# по одному за каждый вызов функции. print_backward может принимать и другие аргументы.
# # должен вывестись осмысленный текст
# print_forward(['сложнее', 'задачу', 'решить', 'можно', 'Теперь'])

def print_backward(n, *args):
    print(n[-1])
    for i in range(1, len(n)):
        return print_backward(n[:len(n)-i])


n = list(map(int, input().split()))
print_backward(n)
