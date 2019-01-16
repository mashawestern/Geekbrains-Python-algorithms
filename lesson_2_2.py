# 2. Посчитать четные и нечетные цифры введенного натурального числа.
#  Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

even=0
odd=0
num = int(input('Введите число: '))
if num < 10:
    if num % 2 == 0:
        even = 1
    else:
        odd = 1
else:
    while num > 9:
        lastdigit = num%10

        if lastdigit%2 == 0:
            even+=1
        else:
            odd+=1
        num = num//10

    if num%2 == 0:
        even+=1
    else:
        odd+=1

print(f'Количество четных цифр {even}\n Колическтво нечётных цифр {odd}')






