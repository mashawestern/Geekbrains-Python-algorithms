#2. Написать два алгоритма нахождения i-го по счёту простого числа.

import cProfile

def sieve(n):
    num = 2            #число в последовательности  2,3,4,5, и т д
    i = 1              #счётчик
    d = 2              #делитель, проверяем кратность следующего числа в последовательности на числа до него
    result = 2
    while i < n:
        num+=1
        while num % d != 0:
              d += 1
        if d == num:
           i+=1
           result = num
        d = 2
    print (result)


# cProfile.run('sieve(100)')

#   5 function calls in 0.000 seconds   n = 10
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Lesson_4_2.py:5(sieve)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# 100 loops, best of 5: 231 usec per loop     n = 10
# 100 loops, best of 5: 96.7 usec per loop    n = 20
# 100 loops, best of 5: 266 usec per loop     n = 40
# 100 loops, best of 5: 351 msec per loop     n = 100


def sieve2(n):
     result = [2]
     num = 2
     while len(result) < n:
          num+=1
          sieve = [i for i in range(num)]
          sieve[1] = 0
          for i in range(2, num):
              if sieve[i] != 0:
                  j = i + i
                  while j < num:
                     sieve[j] = 0
                     j += i

          result = [i for i in sieve if i != 0]
     print(result[n-1])

cProfile.run('sieve2(40)')

#  90 function calls in 0.000 seconds   n = 10
# 28    0.000    0.000    0.000    0.000 Lesson_4_2.py:48(<listcomp>)
#----------------------------
# 216 function calls in 0.001 seconds   n = 20
#  70    0.000    0.000    0.000    0.000 Lesson_4_2.py:48(<listcomp>)
#-----------------------------
# 522 function calls in 0.007 seconds   n = 40
# 172    0.001    0.000    0.001    0.000 Lesson_4_2.py:48(<listcomp>)


# 100 loops, best of 5: 403 usec per loop    n = 10
# 100 loops, best of 5: 700 usec per loop    n = 20
# 100 loops, best of 5: 4.02 msec per loop   n = 40
# 100 loops, best of 5: 43.2 msec per loop   n = 100


# Вывод : если не задан диапазон целых чисел для поиска простых чисел, первый линейный алгоритм работает намного быстрее. Или я слишком намудрила со вторым алгоритмом.