# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке
# [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

import random


def arr_sort(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(-100, 100))
    print(arr)
    print()

    k = 1
    while k < len(arr):
        for i in range(len(arr) - k):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                flag = False        # Флаг были ли перестановки, если перестановок не было, значит все уже отсортировано
        if flag == True:
            break
        flag = True
        print(arr)
        k += 1

    print()
    print(arr)


arr_sort(10)

