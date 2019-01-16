#7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.


import random
size = 10
max_item = 20
min_item = 0
array = [random.randint(min_item, max_item) for _ in range (size)]

print(array)

min_min = array[0]
min_max = array[0]

for i in range(1,size):
    if array[i] <= min_max:
        min_min = min_max
        min_max = array[i]

print(min_max,min_min)