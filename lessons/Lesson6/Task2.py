# Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
# Число положительное целое, произвольной длины.
# Задача требует работать только с числами (без конвертации числа в строку или что-нибудь еще).
n = int(input())
m = n
digits_amount = 0
count_equals = 0
while n > 0:
    digits_amount += 1
    n //= 10
number_of_digits = digits_amount
while digits_amount > 1:
    last_digit = m % 10
    first_digit = m//10**(digits_amount-1)
    if last_digit == first_digit:
        count_equals += 1
    m = (m-first_digit*(10**(digits_amount-1))) // 10
    digits_amount -= 2
if count_equals == number_of_digits//2:
    print("The number is palindrom")
else:
    print("The namber is not palindrom")
