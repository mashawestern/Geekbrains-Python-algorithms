#4. Определить, какое число в массиве встречается чаще всего.

import random

size = 10

max_item = 10
min_item = 0
array = [random.randint(min_item, max_item) for _ in range (size)]

print(array)

num = array[0]
q_max = 1

for i in range(size):
    q = 1
    for j in range (i+1, size):
        if array[j] == array[i]:
            q+=1

    if q > q_max:
       q_max = q
       num = array[i]


print(f'Число {num} встречается в массиве {q_max} раза')





