# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
#  элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
# соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


from collections import deque

a = deque('A2') #input('Введите первое число: '))
b = deque('C4F') #input('Введите второе число: '))

while len(a) > len(b):
    b.appendleft(0)
while len(a) < len(b):
    a.appendleft('0')

c = deque('0123456789ABCDEF')
d = {i : j for i , j in zip(c,range(16))}
d_rev ={i : j for i , j in zip(range(16), c)}
s = [0 for i in range(len(a)+1)]   # сумма
p = [0 for i in range(len(a)*2)]  # произведение

a.reverse()
b.reverse()

for i in range(len(a)):     # сумма
    n = d[a[i]] + d[b[i]]
    s[i]+= n
    s[i+1] += s[i] // 16
    s[i] = s[i] % 16

s.reverse()

s = [d_rev.get(s[i]) for i in range(len(s))]
print (s)


# ------------------------------------ произведение--------------------------------

q = 0
for i in range(len(b)):
    m = d.get(b[i])*(16**i)
    q += m

for i in range(len(a)):
    qq = q
    while qq > 0:
        p[i]+= d[a[i]]
        qq -= 1

for i in range(len(p)-1):
    p[i + 1] += p[i] // 16
    p[i] = p[i] % 16

p.reverse()

p =[d_rev.get(p[i]) for i in range(len(p))]
print(p)

# Решила!!