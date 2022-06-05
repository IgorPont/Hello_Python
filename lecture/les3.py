# def f(x):
#     return x**2


# g = f

# print(type(f))
# print(type(g))

# print(f(4))
# print(g(4))


# def calc(x):
#     return x+10


# print(calc(10))


# def math(op, x):
#     print(op(x))


# math(calc, 10)

# def sum(x, y):
#     return x+y

# # sum = lambda x, y: x+y


# def mylt(x, y):
#     return x*y


# def calc(op, a, b):
#     print(op(a, b))
#     # return op(a, b)


# calc(sum, 4, 5)

# List Comprehension (быстрое составление списка)

# any_list = []

# for i in range(1, 21):
#     any_list.append(i)
# print(any_list)

# a_list = [i for i in range(1, 21) if i % 2 == 0]
# print(a_list)

# def mult(a): return i**2


# a_list = [(i, mult(a)) for i in range(1, 21) if i % 2 == 0]
# print(a_list)

# def select(f, col):
#     return [f(x) for x in col]


# def where(f, col):
#     return [x for x in col if f(x)]


# data = '1 2 3 4 5 6'.split()

# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res = select(lambda x: (x, x**2), res)
# print(res)

# Функция map

# li = [x for x in range(1, 20)]
# print(li)

# li = list(map(lambda x: x+10, li))
# print(li)

# data = list(map(int, input().split()))
# print(data)

# data = [x for x in range(10)]

# res = list(filter(lambda x: not x % 2, data))
# print(res)

# Функция zip

# users = ['user1', 'user2', 'user3']
# ids = [1, 2, 3]

# data = list(zip(users, ids))
# print(data)

# Функция enumerate

users = ['user1', 'user2', 'user3']
ids = [1, 2, 3]

data = list(enumerate(users))
print(data)
