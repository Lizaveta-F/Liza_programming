# В задаче на списки "Развернуть массив" введите индексы l, r, используя кортеж 
# (индексы должны быть заданы в одну строку через пробел)

lst = list(map(int, input().split()))
l_r = tuple((input("Please, enter the left and the right borders:").split()))
l=int(l_r[0])
r=int(l_r[-1])
if l <= r:
    lst_extract = lst[l:r+1]
    lst_extract.reverse()
    lst_final = lst[:l]+lst_extract+lst[r+1:]
else:
    lst_extract = lst[r:l+1]
    lst_extract.reverse()
    lst_final = lst[:r]+lst_extract+lst[l+1:]
print(lst_final)