# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
# для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
# наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий,
# чья прибыль ниже среднего.

from collections import namedtuple

Firm_Form = namedtuple('Firm_Form', 'firm_name, quoter_1, quoter_2, quoter_3, quoter_4, year')

firms = []
n = int(input("Введите количество предприятий: "))
s = 0

for i in range(n):
    firm = Firm_Form(0,0,0,0,0,0,)
    firm = firm._replace(firm_name = input(str(i + 1) + "-е предприятие: "))
    firm = firm._replace(quoter_1 = int(input("Прибыль за первый квартал: ")))
    firm = firm._replace(quoter_2 = int(input("Прибыль за второй квартал: ")))
    firm = firm._replace(quoter_3 = int(input("Прибыль за третий квартал: ")))
    firm = firm._replace(quoter_4 = int(input("Прибыль за четвертый квартал: ")))
    firm = firm._replace(year = sum(firm[1:5]))
    firms.append(firm)
    s+=sum(firm[1:5])
avrg = int(s / n)

print(firms)
print(f'\nСредняя прибыль по предприятиям:{avrg}')
print(f'Предприятия с прибылью выше среднего:')
for i in range(n):
    if firms[i][5] > avrg:
       print(firms[i][0])
print(f'Предприятия с прибылью ниже среднего:')
for i in range(n):
    if firms[i][5] < avrg:
       print(firms[i][0])


# Обидно, что так не получается, не поняла почему.
# for i in firms:
#    if firm.year > avrg:
#       print(firm.firm_name)

