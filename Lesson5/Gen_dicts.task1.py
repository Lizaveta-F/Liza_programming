# Создайте словарь с помощью генератора словарей, так чтобы его ключами были числа от 1 до 20,
# а значениями кубы этих чисел.
dict_1 = {el: el**3 for el in range(1, 21)}
print(dict_1)
