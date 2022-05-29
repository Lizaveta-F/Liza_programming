# Напишите программу, которая считает общую цену. Вводится M рублей и N копеек цена,
# а также количество S товара Посчитайте общую цену в рублях и копейках за L товаров.
rubles = 3
pennies = 11
amount = 5
sum_rubl = (rubles*100+pennies)*amount//100
sum_pen =  (rubles*100+pennies)*amount % 100
print('Общая цена равна', sum_rubl, 'рублей', sum_pen, 'копеек')
