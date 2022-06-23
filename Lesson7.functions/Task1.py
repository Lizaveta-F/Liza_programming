# Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел, 
# отсортированных по возрастанию, которая этот список “сворачивает”.

# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  #  "0-4, 7-8, 10"
# get_ranges([4,7,10])  # "4, 7, 10"
# get_ranges([2, 3, 8, 9])  # "2-3, 8-9"

def get_ranges(a):
    begin=0
    for i in range(len(a)-1):
        if a[i+1]-a[i]==1:
            end_num=i+1
            print(begin,"-",end_num) 
        else:
            end_num=begin     
            print(begin)
get_ranges([4, 7, 8, 10])
    
    