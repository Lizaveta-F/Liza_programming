# Используйте генератор спи-сков чтобы получить следующий: ['xy', 'xz', 'xv', 'yy', 'yz', 'yv'].
k = [i+j for i in 'xy' for j in 'yzv']
print(k)
