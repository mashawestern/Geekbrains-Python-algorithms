# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

n_column = 10
n_row = 5
max_item = 9
min_item = 0

array =[[random.randint(min_item, max_item) for _ in range (n_column)] for _ in range(n_row)]

max_row = min_item

for i in range(n_row):
    for j in range(n_column):
        print(array[i][j], end = "  ")
    print()
for i in range (n_column):
    print('--', end = " ")

print()

for i in range(n_column):
    min_column = array[0][i]
    for j in range(1,n_row):
        if array[j][i] < min_column:
            min_column = array[j][i]
    print( min_column , end = '  ')
    if min_column > max_row:
        max_row = min_column

print()
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы {max_row}')

