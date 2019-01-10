# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random
import cProfile

# Моё решение
def option1(size):
    array = [random.randint(-100, 100) for _ in range(size)]
    idx_max = 0
    idx_min = 0
    for i in range(len(array)):
       if array[i] < array[idx_min]:
          idx_min = i


    for k in range(len(array)):
       if array[k] > array[idx_max]:
          idx_max = k

    #print(f'Min = {array[idx_min]} в ячейке {idx_min}; Max = {array[idx_max]} в ячейке {idx_max}')
    array[idx_min],array[idx_max] = array [idx_max],array[idx_min]
    #print(array)

cProfile.run('option1(100000)')

# 58 function calls in 0.001 seconds      size = 10
# 5272 function calls in 0.004 seconds    side = 1000
# 527451 function calls in 0.226 seconds  side = 100000

# 100 loops, best of 5: 27.2 usec per loop - size 10
# 100 loops, best of 5: 1.57 msec per loop-  size 1000
# 100 loops, best of 5: 160 msec per loop -  size 100000


# Ваше первое решение

def option2(size):
    array = [random.randint(-100, 100) for _ in range(size)]
    idx_max = 0
    idx_min = 0
    for i in range(len(array)):
        if array[i] < array[idx_min]:
           idx_min = i
        elif array[i] > array[idx_max]:
           idx_max = i
    #print(f'Min = {array[idx_min]} в ячейке {idx_min}; Max = {array[idx_max]} в ячейке {idx_max}')

    spam = array[idx_min]
    array[idx_min] = array[idx_max]
    array[idx_max] = spam
    #print(array)

#cProfile.run('option2(10)')

# 58 function calls in 0.001 seconds      size = 10
# 5253 function calls in 0.004 seconds    size = 1000
# 527567 function calls in 0.373 seconds  size = 100000

# 100 loops, best of 5: 27.2 usec per loop - size = 10
# 100 loops, best of 5: 1.54 msec per loop - size = 1000
# 100 loops, best of 5: 157 msec per loop -  size = 100000





# Ваше второе решение
def option3(size):
    array = [random.randint(-100, 100) for _ in range(size)]
    min_num = min(array)
    max_num = max(array)
    idx_min = array.index(min_num)
    idx_max = array.index(max_num)
    #print(f'Min = {array[idx_min]} в ячейке {idx_min}; Max = {array[idx_max]} в ячейке {idx_max}')
    array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
    # print(array)


#cProfile.run('option3(10)')
# 63 function calls in 0.000 seconds     size = 10
# 5315 function calls in 0.004 seconds   size = 1000
# 527543 function calls in 0.350 second  size = 100000


# 100 loops, best of 5: 25.8 usec per loop  size = 10
# 100 loops, best of 5: 1.43 msec per loop  size = 1000
# 100 loops, best of 5: 143 msec per loop   size = 100000

# Вывод: измерения для разных алгоритмов совпадают. Наибольшее время тратится на создание массива случайных чисел. Задача слишком простая ,что бы можно было сделать по измерениям вывод какой алгоритм эффективнее. Побоялась задавать больший размер строки,
#  вдруг зависнет компьютер. Но по логике ваше первое решение наиболее эффективно из трёх, так как только за один проход по списку находит минимальное и максимальное число.