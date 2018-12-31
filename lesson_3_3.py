#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

size = 10
max_item = 20
min_item = -20
array = [random.randint(min_item, max_item) for _ in range (size)]

print(array)

max_num = min_item
min_num = max_item


for i in range(len(array)):
    if array[i] < min_num:
        min_num = array[i]
        n = i

for k in range(len(array)):
    if array[k] > max_num:
        max_num = array[k]
        m = k

array[n],array[m] = array [m],array[n]
print(array)





