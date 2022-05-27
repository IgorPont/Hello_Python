# 1. Напишите программу, которая принимает на вход вещественное число и показывает
# сумму его цифр(отсекаем минус, считаем все в плюс).
# *Пример:*
# - 67.82 -> 23
# - 0.56 -> 11

import random


def sum_digits_number(num):
    str_num = str(num)
    str_num = str_num.replace('.', '').replace('-', '')
    str_num = list(str_num)
    str_num = map(int, str_num)
    res = sum(str_num)
    return res

# num_user = float(input('Enter a real number: '))
# print(f'The sum of digits in the number is {sum_digits_number(num_user)}')

# 2. Напишите программу, которая принимает на вход число N и выдает
# набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def factorial_sequence(num):
    res = []
    fact = 1
    for i in range(1, num + 1):
        fact *= i
        res.append(fact)
    return res


# num_user = int(input('Enter the number: '))
# print(
#     f'The set of products of numbers from 1 to {num_user}:\n{factorial_sequence(num_user)}')

# 3. Реализуйте случайное перемешивания списка.
# *Пример:*
# Исходный вариант -> ['Веселый пианист', 250, 3.14, 'True ']
# Результат -> [250, 3.14, 'True ', 'Веселый пианист']


def list_shuffle(any_lst):
    random.shuffle(any_lst)
    return any_lst


lst_user = ['Веселый пианист', 250, 3.14, 'True ']
print(f'Result: {list_shuffle(lst_user)}')
