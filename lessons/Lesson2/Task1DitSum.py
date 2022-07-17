n = int(input())
if -999 <= n <= 999:
    if -9 <= n <= 9:
        print("Сумма цифр =", abs(n))
    elif 10 <= n <= 99 and -99 <= n <= -10:
        n2_units = abs(n) % 10
        n2_dozens = abs(n)//10
        sum_of_2dit = n2_units+n2_dozens
        print("Сумма цифр =", sum_of_2dit)
    else:
        n3_units = abs(n) % 10
        n3_hund = abs(n)//100
        n3_dozens = abs(n)//10 % 10
        sum_of_3dit = n3_units + n3_hund+n3_dozens
        print("Сумма цифр =", sum_of_3dit)
else:
    print("Ошибка вводимых данных")
