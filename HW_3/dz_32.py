# Напишите программу, которая найдёт произведение пар
#  чисел списка. Парой считаем первый и последний элемент,
#  второй и предпоследний и т.д.

from random import randint, random
n = int(input('Ввести длину списка: ' ))
arr =[]
for i in range (n):
    arr.append(randint(1,10))
print(arr)
for i in range((len(arr) + 1)//2):
    a = arr[i] * arr[len(arr)-i-1]
    print(a, end =' ')
