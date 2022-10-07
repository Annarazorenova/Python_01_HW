# Задайте список из N элементов, заполненных числами из 
# промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. 
# Позиции вводятся через пробел в одной строкой.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# '0 2 4'
# res -

from random import randint
numbers = []
for i in range(10):
    numbers.append(randint (-10,10))
print(numbers)

def get_numbers(numbers):
    count =0 
    for element in numbers:
        count +=1
    return count
print('Number of elements: ', get_numbers(numbers))

x = int(input('Enter  position of first element: '))
y = int(input('Enter position of second element: '))

for i in range(len(numbers)):
    mult = numbers[x] * numbers[y]
print(mult) 









