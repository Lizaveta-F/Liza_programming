# Минимум, медиана, максимум
# Дан некоторый список из чисел. Необходимо вывести минимум, медиану) и
# максимум из элементов для этого списка.
# Список интов из stdin можно прочитать следующим образом:
# arr = list(map(int, input().split()))
# водить надо числа через пробел в одну строку


lst = list(map(int, input().split()))
lst.sort()
max_el = lst[-1]
min_el = lst[0]
median_el = int((len(lst)-1)/2)
if len(lst) % 2 != 0:
    median_final = lst[median_el]
else:
    median_final = (lst[median_el]+lst[median_el+1])/2
print(min_el, median_final, max_el)
