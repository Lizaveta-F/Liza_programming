def is_prime(n):
    return all([True if n % i != 0 else False for i in range(2, n)])


n = int(input())
print(is_prime(n))
