# Напишите программу, которая принимает на вход число N и
#  выдает набор произведений чисел от 1 до N.

n = int(input('Enter number: '))
mult = 1
list = []
for i in range(1, n+1):
    mult *=i
    list.append(mult)
print(list, end =' ')

