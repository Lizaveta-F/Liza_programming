n = int(input())
if 1000 <= n <= 9999:
    last_digit = n % 10
    third_digit = (n//10) % 10
    second_digit = (n//100) % 10
    first_digit = n//1000
    if first_digit == last_digit and third_digit == second_digit:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
