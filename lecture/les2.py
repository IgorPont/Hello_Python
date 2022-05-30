# # Запись данных в файл
# colors = ['red', 'green', 'blue123']
# data = open('file.txt', 'a')
# # data.writelines(colors) # разделителей не будет
# data.write('LINE 2\n')
# data.write('LINE 3\n')
# data.close()  # закрывает подключение к файлу (обязательно после окончания работы)

# exit()  # останавливает выполнение кода

# # иной способ (разрыв связи происходит автоматически)
# with open('file.txt', 'a') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

# # Чтение данных из файла
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# import les as h
# import les

# print(les.f(1))

# # Использование псевдонима

# print(h.f(1))


# def new_string(arg, count=3):
#     return arg*count


# print(new_string('$'))
# print(new_string(2))

# def concatenation(*params):
#     res: str = ""  # переменной res указан тип данных
#     for item in params:
#         res += item
#     return res


# print(concatenation('a', 'b', 'c'))

list1 = [1, 2, 3, 4, 5]
list1.pop()  # удаление последнего элемента списка

list1 = [1, 2, 3, 4, 5]
list1.pop(2)  # удаление элемента списка по индексу

list1 = [1, 2, 3, 4, 5]
# добавление элемента на конкретную позицию (место элемента, сам элемент)
list1.insert(2, 11)

list1 = [1, 2, 3, 4, 5]
list1.append(11)  # добавление элемента в конец списка
