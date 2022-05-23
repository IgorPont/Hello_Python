# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

from pickletools import string4


def сheck_square_number(num_1, num_2):
    if num_1*num_1 == num_2:
        print(f'Число {num_2} явялется квадратом числа {num_1}')
    else:
        print(f'Число {num_2} не явялется квадратом числа {num_1}')

# num_user_1 = int(input(f'Введите первое число: '))
# num_user_2 = int(input(f'Введите второе число: '))
# сheck_square_number(num_user_1, num_user_2)

# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.


def max_numbers_user():
    max = int(input('Введите число: '))
    for i in range(4):
        num_us = int(input('Введите число: '))
        if num_us > max:
            max = num_us
    return max

# print(max_numbers_user())

# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от - N до N


def range_negative_positive(num):
    r = range(-num, num+1)
    for i in r:
        print(i, end=' ')


# num_user = int(input('Введите число: '))
# range_negative_positive(num_user)


# 4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

def print_first_num_fraction(num):
    number = str(num - int(num))
    number = number[2]
    if number == '0':
        return 'Первой цифры дробной части нет'
    else:
        return number

# num_user = float(input('Введите число: '))
# print(print_first_num_fraction(num_user))

# Альтернативное решение
# x = float(input())
# x = int((x*10) % 10)
# print(x)

# 5. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.


def check_multiplicity(num):
    if (num % 5 == 0 and num % 10 == 0 or num % 15 == 0) and num % 30 != 0:
        return True
    else:
        return False


# num_user = int(input('Введите число: '))
# print(check_multiplicity(num_user))

# 6. На столе стоит две корзины с яблоками. Корзина a и корзина b. Введите  количество яблок с клавиатуры. Затем поменяйте содержимое корзин местами и выведите результат.

def chenge_basket(arg):
    temp = arg[1]
    arg[1] = arg[0]
    arg[0] = temp
    return arg


# basket_1 = int(input('Введите количество яблок в первой корзине: '))
# basket_2 = int(input('Введите количество яблок во второй корзине: '))
# two_basket = [basket_1, basket_2]
# print(two_basket)
# print(chenge_basket(two_basket))


# 7. Пишем "компьютерный вирус". Запросите у пользователя любой текст. Сохраните вторую с начала и третью с конца буквы в отдельные переменные (например a и b). Замените во всём тексте букву из переменной a, на букву из переменной b и выведите зашифрованный текст на экран.

def computer_virus(string):
    a = string[1]
    b = string[-3]
    string = string.replace(a, b)
    return string

# text = input('Введите любой текст:\n')
# modif_text = computer_virus(text)
# print(modif_text)

# 8. Напишите программу, которая проверит истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y


x = True
y = False
if not(x or y) is (not(x) and not(y)):
    print('Высказывание истинно')
else:
    print('Высказывание ложно.')
