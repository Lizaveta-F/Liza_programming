def sum_simp(a):
    summa = 0
    for i in a:
        counter = 0
        i = int(i)
        for j in range(1, i+1):
            if i % j == 0:
                counter += 1
        if counter <= 2:
            summa += i
    counter2 = 0
    for i in range(1, summa+1):
        if summa % i == 0:
            counter2 += 1
    if counter2 <= 2:
        print(summa, "YES", sep='\n')
    else:
        print(summa, "NO", sep='\n')


a = list(map(str, input().split()))
sum_simp(a)
