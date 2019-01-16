# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

import random

size = 10
max_item = 20
array = [random.randint(0, max_item) for _ in range (size)]

print(array)

n = 0
array_even_index = []
for i in range(len(array)):
    if array[i] %2 == 0:
        array_even_index.append(n)
    n+=1
print(array_even_index)





