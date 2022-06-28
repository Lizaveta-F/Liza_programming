# Реализовать декоратор timeit, который должен засекать время работы декорируемой функции.
# Декоратор опционально должен принимать параметр количество замеров (вызовов функции) и
# возвращать среднее время выполнения функции. Используйте time из модуля time, как в примерах
# @timeit(n=5)
# def foo(n):
#     return sum(range(n))

# foo(1000) должно вернуться усредненное время выполнения этой функции


from time import time


def time_it(func):
    def wrapper(n):
        start = time()
        result = func(n)
        print(f'{(time()-start):.6f}s')
        return result
    return wrapper


@time_it  # декорирование функции
def to_sum(n):
    summa = 0
    for i in range(n):
        summa += i


n = int(input())
to_sum(n)
