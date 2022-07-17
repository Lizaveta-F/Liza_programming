# Реализовать функцию print_forward, принимающую на вход список.
# Данная функция должна рекурсивно выводить элементы этого списка в stdout по одному за каждый
# вызов функции. print_forward может принимать и другие аргументы.
# # должен вывестись осмысленный текст
# print_forward(['Это', 'игрушечный', 'пример', 'не', 'используйте', 'рекурсию', 'для', 'такого'])

def print_forward(n, *args):
    print(n[0])
    for i in range(1, len(n)):
        return print_forward(n[i:])


n = list(map(str, input().split()))
print_forward(n)
