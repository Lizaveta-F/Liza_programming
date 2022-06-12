n = int(input())
# if abs(n) <= 9:
#     print("Сумма цифр =", abs(n))
# elif 10 <= abs(n) <= 99:
#     n2_units = abs(n) % 10
#     n2_dozens = abs(n)//10
#     sum_of_2dit = n2_units+n2_dozens
#     print("Сумма цифр =", sum_of_2dit)
# elif 100 <= abs(n) <= 999:
#     n3_units = abs(n) % 10
#     n3_hund = abs(n)//100
#     n3_dozens = abs(n)//10 % 10
#     sum_of_3dit = n3_units + n3_hund+n3_dozens
#     print("Сумма цифр =", sum_of_3dit)
# else:
#     print("Ошибка вводимых данных")
if n > 999:
    print('wrong data')
else:
    n_units = abs(n) % 10
    n_dozens = abs(n)//10 % 10
    n_hund = abs(n)//100
    print(n_hund + n // 10 % 10 + n_units)
