# Используйте на предыдущий список slice чтобы получить следующий: ['xy', 'xv', 'yz'].
k = [i+j for i in 'xy' for j in 'yzv']
k_sliced = slice(0, len(k)+1, 2)
print(k[k_sliced])
