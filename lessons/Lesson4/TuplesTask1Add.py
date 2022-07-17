# Максимальный элемент
# В целочисленном массиве A[1..N] на отрезке [L,R] необходимо найти максимальный элемент и его номер.

n = int(input())
lst = list(map(int, input("Please enter the list: ").split()))
l_r = list(map(int, input("Please enter left and right borders: ").split()))
l_r_extract = lst[l_r[0]-1:l_r[1]]
max_el = max(l_r_extract)
print(max_el, lst.index(max_el))
