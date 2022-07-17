def isprime(num):
    i = 2
    while(i < num):
        if num % i == 0:
            return False
        i += 1
    return True


def goldbach(num):
    for i in range(2, num):
        if isprime(i):
            if isprime(num-i):
                print(num, '=', i, '+', num-i)
                return True
    return False


num = int(input("Enter the number: "))
goldbach(num)
