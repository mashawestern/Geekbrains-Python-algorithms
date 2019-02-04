#3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
#Например, если введено число 3486, то надо вывести число 6843.

num = int(input('Введите число: '))
reversenum=0
while num > 9:
    lastdigit = num%10
    reversenum = reversenum*10+lastdigit
    num = num//10

reversenum = reversenum * 10 + num

print(f'Число в обратном порядке цифр {reversenum}')






