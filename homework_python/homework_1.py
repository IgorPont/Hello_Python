# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

import math


def check_weekend(num):
    if num > 0 and num < 6:
        return 'The day of the week is a weekday'
    elif num == 6 or num == 7:
        return 'The specified day of the week is a weekend'
    else:
        return 'The number entered does not correspond to the day of the week'


# num_user = int(input('Enter the number for the day of the week: '))
# print(check_weekend(num_user))


# 2. Напишите программу, которая принимает на вход координаты точки (X и Y), и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

def plane_quarter_number(x, y):
    if x > 0 and y > 0:
        return 'The set point is in the first (I) coordinate plane'
    elif x < 0 and y > 0:
        return 'The set point is in the second (II) coordinate plane'
    elif x < 0 and y < 0:
        return 'The set point is in the third (III) coordinate plane'
    elif x > 0 and y < 0:
        return 'The set point is in the fourth (IV) coordinate plane'
    elif x == 0 and y != 0:
        return 'The point is on the y-axis'
    elif x != 0 and y == 0:
        return 'The point is on the x-axis'
    else:
        return 'You have entered the zero coordinates of the point'


# coor_x = float(input('Enter the coordinates of the point on the x-axis: '))
# coor_y = float(input('Enter the coordinates of the point on the y-axis: '))
# print(plane_quarter_number(coor_x, coor_y))


# 3. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def quarter_coordinate_range(num):
    if num >= 1 and num <= 4:
        if num == 1:
            return 'For the first plane, the range of coordinates \nwhere x > 0 and y > 0 is defined'
        elif num == 2:
            return 'For the second plane, the range of coordinates \nwhere x < 0 and y > 0 is defined'
        elif num == 3:
            return 'For the third plane, the range of coordinates where x < 0 and y < 0 is defined'
        elif num == 4:
            return 'For the fourth plane the range of coordinates where x > 0 and y < 0 is defined'
    else:
        return 'There is no such plane of coordinates'


# quarter_num = int(input('Enter the number of the coordinate plane: '))
# print(quarter_coordinate_range(quarter_num))

# 4. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.


def distance_two_points(xA, yA, xB, yB):
    result = math.sqrt(((xB-xA)**2) + ((yB-yA)**2))
    return math.floor(result * 100)/100


x_point_A = float(input('Enter the coordinates of point A on the x-axis: '))
y_point_A = float(input('Enter the coordinates of point A on the y-axis: '))
x_point_B = float(input('Enter the coordinates of point B on the x-axis: '))
y_point_B = float(input('Enter the coordinates of point B on the y-axis: '))
print(distance_two_points(x_point_A, y_point_A, x_point_B, y_point_B))
