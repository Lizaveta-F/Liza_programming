def F(n, k):
    fact_n = 1
    fact_k = 1
    fact_nk = 1
    for i in range(1, n+1):
        fact_n *= i
    for i in range(1, k+1):
        fact_k *= i
    for i in range(1, n-k+1):
        fact_nk *= i
    matches = (fact_n)/(fact_k*(fact_nk))
    print(int(matches))


F(7, 3)
