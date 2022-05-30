# Переменные
# int, float, boolean, str, list, None

# value = None  # присвоено пустое значение переменной
# a = 123  # print(type(a)) - показывает тип переменной
# b = 1.23
# print(a)
# print(b)

# value = 123
# print(type(value))

# str = 'hello "word"'  # можно так str = "hello 'word'"
# print(str)  # вывод строки
# print(a, '-', b, '-', str)
# print('{} - {} - {}'.format(a, b, str))
# print('{2} - {1} - {0}'.format(a, b, str))  # указать порядок вывода
# print(f'{a} - {b} - {str}')

# f = True
# print(f)

# список
# list = [1, 2, 3, 'hello', True]  # но так нельзя, лучше одного типа
# print(list)

# Получение данных

# print('Input a')
# a = int(input())  # по умолчанию переменная имеет строковое значение, чтобы указать конкретный тип, нужно добавить значение типа перед командой запроса переменной
# print('Input b')
# b = int(input())
# print(a, b, a+b)
# print(f'{a} {b}')

# Условия выполняются попорядку (elif может быть много)

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# elif a < b:
#     print(b)
# else:
#     print('Числа равны')

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
