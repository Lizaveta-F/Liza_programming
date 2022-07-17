def dig_amount(a):
    n = 0
    for i in a:
        if 97 <= ord(i) <= 122 or 65 <= ord(i) <= 90:
            n += 1
    print(n)


a = list(map(str, input().split()))
dig_amount(a)
