# Задача 33.
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 10) многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# print('a = 2\u00B2') # красивая запись степени

from random import randint
import itertools


def list_ratios(k):
    ratios = [randint(0, 10) for i in range(k + 1)]
    if ratios[0] == 0:
        ratios[0] = randint(1, 10)
    return ratios


def list_polynomial(cof, ratios):
    op = ['*x^']*(cof-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c in itertools.zip_longest(
        ratios, op, range(cof, 1, -1), fillvalue='') if a != 0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x', ' x')


cof = randint(2, 5)
ratios = list_ratios(cof)
polynom = list_polynomial(cof, ratios)
print(polynom)

with open('Polynomial_task_33.txt', 'w') as data:
    data.write(polynom)
