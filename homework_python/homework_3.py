import random


def check_natural_num(number):
    while number <= 0:
        number = int(input('Enter a natural number, try again: '))
    return number


def add_list_random_num(num):
    new_list = []
    for item in range(0, num):
        item = random.randint(1, 9)
        new_list.append(item)
    return new_list


def sum_odd_items(any_list):
    res = 0
    pos = len(any_list)
    for i in range(1, pos, 2):
        res += any_list[i]
    return res


def product_number_pairs(some_list):
    res_list = []
    len_list = len(some_list)
    half = int(len_list/2)
    if len_list == 1:
        res_list.append(some_list[0]**2)
        return res_list
    elif len_list % 2 == 0:
        for i in range(0, half):
            res_list.append(some_list[i]*some_list[len_list - i - 1])
        return res_list
    else:
        for i in range(0, half):
            res_list.append(some_list[i]*some_list[len_list - i - 1])
        res_list.append(some_list[half+1]**2)
        return res_list


def diff_fract(a_list):
    fract_list = []
    for i in a_list:
        fract_list.append(round((i % 1)*100))
    diff_num = max(fract_list) - min(fract_list)
    result = diff_num / 100
    return result

# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


# num_user = check_natural_num(
#     int(input('Enter the number of items in the list: ')))
# user_list = add_list_random_num(num_user)
# print(f'Source list: {user_list}')
# print(
#     f'The sum of odd elements in the list is equal: {sum_odd_items(user_list)}')


# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Если остается 1 элемент без пары - умножаем его самого на себя.
# Пример:
# - [2, 3, 4, 5, 6] = > [12, 15, 16]
# - [2, 3, 5, 6] = > [12, 15]

# num_item = check_natural_num(
#     int(input('Enter the number of items in the list: ')))
# fill_list = add_list_random_num(num_item)
# print(f'Source List: {fill_list}')
# prod_prs = product_number_pairs(fill_list)
# print(f'The product of the pairs: {prod_prs}')


# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] = > 0.19


source_list = [1.1, 1.2, 3.1, 5.05, 10.01]
print(f'The difference is: {diff_fract(source_list)}')
