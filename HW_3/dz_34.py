# Напишите программу, которая будет преобразовывать
#  десятичное число в двоичное.

def binary():
    n = int(input('Enter decimal number: '))
    bin = (' ')
    while n > 0:
        bin =  bin + str(n % 2)
        n //=2
    return bin[::-1]
print(binary())     