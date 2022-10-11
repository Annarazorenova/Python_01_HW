# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной
#  позиции.

from random import randint
numbers = []
for i in range(10):
    numbers.append(randint (1,10))
print(numbers)
summ = 0 
for i in range(1, len(numbers), 2):
  summ += numbers[i]
print(summ) 
