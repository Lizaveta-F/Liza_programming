# Минимум, медиана, максимум
# Дан некоторый список из чисел. Необходимо вывести минимум, медиану) и
# максимум из элементов для этого списка.
# Список интов из stdin можно прочитать следующим образом:
# arr = list(map(int, input().split()))
# водить надо числа через пробел в одну строку

import math
lst = list(map(int, input().split()))
lst.sort()
max_el = lst[-1]
min_el = lst[0]
median_el = (len(lst)-1)/2
median_until = int(lst[math.floor(median_el)])
median_after = int(lst[math.ceil(median_el)])
median_final = int((median_until+median_after)/2)
print(min_el, median_final, max_el)
