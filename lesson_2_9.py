# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
#  Вывести на экран это число и сумму его цифр.

biggest_num = 0
summa = 0
answer = 'Y'

while answer == 'Y':
    num = int(input('Введите любое натуральное число :  '))
    if num > biggest_num:
         biggest_num = num
         while num > 9:
            num = num%10
            summa = summa + num
         summa = summa + num

    print(' Еще число? Y/N : ')
    answer = input().upper()
print(f'Наибольшее по сумме цифр число из введеных  {biggest_num}, сумма его цифр {summa}')

