# Развернуть массив
# По аналогии с прошлой задачей дан список целых чисел. Кроме того, даны еще два числа l, r, которые обозначают
# левую границу и правую границу подотрезка в массиве, который надо будет отразить.
# Достаточно лишь вывести результирующий список.
# Индексы могут быть отрицательными

lst = list(map(int, input().split()))
l, r = int(input("Please, enter the left border:")), int(input("Please, enter the right border:"))
if l <= r:
    lst_extract = lst[l:r+1]
    lst_extract.reverse()
    lst_final = lst[:l]+lst_extract+lst[r+1:]
else:
    lst_extract = lst[r:l+1]
    lst_extract.reverse()
    lst_final = lst[:r]+lst_extract+lst[l+1:]
print(lst_final)
