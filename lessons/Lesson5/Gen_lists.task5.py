# Скопируйте список и добавьте в него элемент 2x так чтобы в исходном списке этого элемента не было.
import copy
lst1 = [str(el)+'x' for el in range(1, 5)]
lst1.remove('2x')
lst2 = copy.deepcopy(lst1)
lst2.append("2x")
# lst2_2=copy.deepcopy(lst1)
# lst2=lst2_2.append('2x')
print("List №1: ", lst1, "List №2: ", lst2, sep='\n')
