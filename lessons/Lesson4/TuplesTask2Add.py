# Ближайшее число
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу xdrlib

N = int(input())
lst = list(map(int, input("Please enter the list: ").split()))
X = int(input())
m = min(lst, key=lambda x: abs(x-X))
print(m)
