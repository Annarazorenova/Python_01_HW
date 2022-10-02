# Напишите программу, которая принимает на вход координаты
#  двух точек и находит расстояние между ними в 2D пространстве.

x1 = float(input('Enter coord x1: '))
y1 = float(input('Enter coord y1: '))
x2 = float(input('Enter coord x2: '))
y2 = float(input('Enter coord y2: '))

print(round(((x2 - x1)**2 + (y1 - y2)**2)**(1/2),  2))