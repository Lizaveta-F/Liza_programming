# Реализовать функцию-генератор, реализующую полный функционал built-in-функции range.
# так делать не надо =))))
# def myrange(*args, **kwargs):
#     yield from range(*args, **kwargs)
# должно выводиться одно и то же
# не забывайте и про отрицательный шаг
# for i in myrange(1, 10, 2):
#     print(i, end=' ')
# print()
# for i in range(1, 10, 2):
#     print(i, end=' ')
# Кстати yield from iterable будет yield'ить элементы из iterable один за другим. Точно так же, как

# for el in iterable:
#     yield el
def my_range(first, second, step):
    number = first
    if step > 0:
        while (number < second):
            yield number
            number += step
    else:
        while (number > second):
            yield number
            number += step

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
step = int(input("Enter the step: "))
k = my_range(start, end, step)

print(*list(k))
