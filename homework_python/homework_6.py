# ===Задача 34.===
# Даны два файла в каждом из которых находится запись многочлена.
# Сформировать файл содержащий сумму многочленов.


# import re
# import itertools


# # Получение данных из файла
# def get_data(file):
#     with open(file, 'r') as data:
#         res = data.read()
#     return res


# # Преобразование полученной строки в списки кортежей каждого полинома
# def string_to_list_tuple(pol):
#     pol = re.sub("[*|^| ]", " ", pol).split('+')
#     pol = [char.split(' ') for char in pol]
#     pol = [[x for x in list if x] for list in pol]
#     for i in pol:
#         if i[0] == 'x':
#             i.insert(0, 1)
#         if i[-1] == 'x':
#             i.append(1)
#         if len(i) == 1:
#             i.append(0)
#     pol = [tuple(int(x) for x in j if x != 'x') for j in pol]
#     return pol


# # Формирование списка кортежей суммы полиномов
# def fold_pols(pol1, pol2):
#     x = [0] * (max(pol1[0][1], pol2[0][1] + 1))
#     for i in pol1 + pol2:
#         x[i[1]] += i[0]
#     res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
#     res.sort(key=lambda r: r[1], reverse=True)
#     return res


# # Составление итогового полинома
# def get_sum_pol(pol):
#     var = ['*x^'] * len(pol)
#     coefs = [x[0] for x in pol]
#     degrees = [x[1] for x in pol]
#     new_pol = [[str(a), str(b), str(c)]
#                for a, b, c in (zip(coefs, var, degrees))]
#     for x in new_pol:
#         if x[0] == '0':
#             del (x[0])
#         if x[-1] == '0':
#             del (x[-1], x[-1])
#         if len(x) > 1 and x[0] == '1' and x[1] == '*x^':
#             del (x[0], x[0][0])
#         if len(x) > 1 and x[-1] == '1':
#             del x[-1]
#             x[-1] = '*x'
#         x.append(' + ')
#     new_pol = list(itertools.chain(*new_pol))
#     new_pol[-1] = ' = 0'
#     return "".join(map(str, new_pol))


# # Запись в файл
# def write_to_file(file, pol):
#     with open(file, 'w') as data:
#         data.write(pol)


# file_1 = '/Users/igor/Desktop/belive/study_projects/HelloPython/homework_python/files_homework_tasks/task_34_polynom_1.txt'
# file_2 = '/Users/igor/Desktop/belive/study_projects/HelloPython/homework_python/files_homework_tasks/task_34_polynom_2.txt'
# file_sum = '/Users/igor/Desktop/belive/study_projects/HelloPython/homework_python/files_homework_tasks/task_34_sum_polynom.txt'

# pol1 = get_data(file_1)
# pol2 = get_data(file_2)
# new_pol1 = string_to_list_tuple(pol1)
# new_pol2 = string_to_list_tuple(pol2)

# sum = get_sum_pol(fold_pols(new_pol1, new_pol2))
# write_to_file(file_sum, sum)

# print(pol1)
# print(pol2)
# print(sum)


# --------------------------------------------------------------------------------

# ===Задача 39.===
# Помните игру с конфетами из модуля "Математика и Информатика"? Создайте такую игру для игры человек против человека
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом"


# from random import randint, choice

# greeting = ('Здравствуйте! Вас приветствует игра "Забери все конфеты!" '
#             'Основные правила игры: '
#             'Нам будет дано некоторое количество конфет, '
#             'за один ход мы можем взять не более определённого количества, '
#             'о котором мы с вами договоримся. '
#             'Итак, начнём!')

# messages = ['Ваша очередь брать конфеты', 'возьмите конфеты',
#             'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'Ваш ход']


# def introduce_players():
#     player1 = input('Давайте познакомися. Как Вас зовут?\n')
#     player2 = 'Робот'
#     print(f'Очень приятно, меня зовут {player2}')
#     return [player1, player2]


# def get_rules(players):
#     n = int(input('Сколько конфет будем разыгрывать?\n '))
#     m = int(input('Сколько максимально будем брать конфет за один ход?\n '))
#     first = int(input(
#         f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу\n'))
#     if first != 1:
#         first = 0
#     return [n, m, int(first)]


# def play_game(rules, players, messages):
#     count = rules[2]
#     print(count)
#     if rules[0] % 10 == 1 and 9 > rules[0] > 10:
#         letter = 'а'
#     elif 1 < rules[0] % 10 < 5 and 9 > rules[0] > 10:
#         letter = 'ы'
#     else:
#         letter = ''
#     while rules[0] > 0:
#         if not count % 2:
#             move = rules[0] % rules[1] + 1
#             print(f'Я забираю {move}')
#         else:
#             print(f'{players[0]}, {choice(messages)}')
#             move = int(input())
#             if move > rules[0] or move > rules[1]:
#                 print(
#                     f'Это слишком много, можно взять не более {rules[1]} конфет{letter}, у нас всего {rules[0]} конфет{letter}')
#                 attempt = 3
#                 while attempt > 0:
#                     if rules[0] >= move <= rules[1]:
#                         break
#                     print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
#                     move = int(input())
#                     attempt -= 1
#                 else:
#                     return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
#         rules[0] = rules[0] - move
#         if rules[0] > 0:
#             print(f'Осталось {rules[0]} конфет{letter}')
#         else:
#             print('Все конфеты разобраны.')
#         count += 1
#     return players[not count % 2]


# print(greeting)

# players = introduce_players()
# rules = get_rules(players)

# winer = play_game(rules, players, messages)
# if not winer:
#     print('У нас нет победителя.')
# else:
#     print(
#         f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')


# --------------------------------------------------------------------------------

# ===Задача 42.===
# Реализовать RLE алгоритм. Реализовать модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах

def get_data_from_file(link):
    data = open(link, 'r')
    in_str = data.read()
    data.close()
    return in_str


def push_encode_file(str, link):
    with open(link, 'w') as data:
        data.write(str)


def rle_encode(data):
    encode = ''
    pr_char = ''
    count = 1

    if not data:
        return ''
    for char in data:
        if char != pr_char:
            if pr_char:
                encode += str(count) + pr_char + ' '
            count = 1
            pr_char = char
        else:
            count += 1
    encode += str(count) + pr_char + ' '
    return encode


def rle_decode(data):
    decode = ''
    count = ''
    i = 0
    while i <= (len(data)-1):
        count += data[i]
        if data[i] == ' ':
            decode += data[i - 1] * int(count[:-2])
            count = ''
        i += 1
    return decode


inp_link = '/Users/igor/Desktop/belive/study_projects/HelloPython/homework_python/files_homework_tasks/task_42_input_data.txt'
out_link = '/Users/igor/Desktop/belive/study_projects/HelloPython/homework_python/files_homework_tasks/task_42_outputs_data.txt'

inp_data = get_data_from_file(inp_link)
code = rle_encode(inp_data)
push_encode_file(code, out_link)

print(inp_data)
print(code)
print(rle_decode(code))
