def dig_amount(a):
    n = 0
    for i in a:
        if i.isdigit():
            n += 1
    print(n)


a = list(map(str, input().split()))
dig_amount(a)
