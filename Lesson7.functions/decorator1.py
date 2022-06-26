# Реализовать декоратор timeit, который должен засекать время работы декорируемой функции. 
# Декоратор опционально должен принимать параметр количество замеров (вызовов функции) и 
# возвращать среднее время выполнения функции. Используйте time из модуля time, как в примерах
# @timeit(n=5)
# def foo(n):
#     return sum(range(n))

# foo(1000) должно вернуться усредненное время выполнения этой функции

from datetime import datetime 

def time_it(func):
    def wrapper(*args,**kwargs):
        start = datetime.time()
        result = func(*args,**kwargs)
        print(datetime.time()-start)
        return result
    return wrapper

@time_it  # декорирование функции
def summa(n):
    summa=0
    for i in range(n):
        summa+=i
    return summa
n=int(input())


