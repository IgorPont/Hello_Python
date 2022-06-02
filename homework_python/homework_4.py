# 1. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# # 45 -> 101101
# 3 -> 11
# 2 -> 10

def binary_number(num):
    count = 0
    new_num = num
    while new_num > 0:
        new_num //= 2
        count += 1
    bin = ''
    for i in range(count):
        bin += str(num % 2)
        num //= 2
    bin = bin[::-1]
    return bin


dec_num = int(input('Enter a positive decimal number: '))
bin_n = binary_number(dec_num)
print(f'Binary representation of a number {dec_num} is: {bin_n}')


# 2. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:*
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# def negafibonacci(num):
#     if num >= 0:
#         seq = range(num + 1)
#         f_list = [0, 1]
#         for i in seq[2:]:
#             f_list.append(f_list[i-1] + f_list[i-2])
#         return f_list[num]
#     else:
#         num = -(num - 1)
#         seq = range(num + 1)
#         f_list = [0, 1]
#         for i in seq[2:]:
#             f_list.append(f_list[i-2] - f_list[i-1])
#         return f_list[num]


# num_us = int(input('Inter the number: '))
# nf = []
# for i in range(-num_us+1, num_us+1):
#     nf.append(negafibonacci(i))
# print(f'For the number {num_us} the negafibonacci sequence is\n{nf}')

# 3. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

# def min_max_num(any_str):
#     num_list = any_str.split()
#     num_list = [int(i) for i in num_list]
#     min = num_list[0]
#     max = num_list[1]
#     if min > max:
#         min, max = max, min
#     for i in range(2, len(num_list)):
#         if num_list[i] > max:
#             max = num_list[i]
#         elif num_list[i] < min:
#             min = num_list[i]
#     return max, min


# set_num = input(
#     'Enter the numbers one after the other,\nseparated by a space: ')
# res = min_max_num(set_num)
# print(f'Maximum number: {res[0]}\nMinimal number: {res[1]}')


# 4. Задайте два целых числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

# def find_lcm(num1, num2):
#     if num1 > num2:
#         min = num2
#     else:
#         min = num1
#     for i in range(1, min + 1):
#         if (num1 % i == 0) and (num2 % i == 0):
#             hcf = i
#     lcm = int((num1 * num2) / hcf)
#     return lcm


# n1 = int(input('Inter the number 1: '))
# n2 = int(input('Inter the number 2: '))
# res = find_lcm(n1, n2)
# print(f'Least common multiple of the numbers {n1} and {n2} is {res}')
