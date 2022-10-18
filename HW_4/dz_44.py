# Задана натуральная степень k. Сформировать случайным
#  образом список коэффициентов (значения от 0 до 100)
#  многочлена и записать в файл многочлен степени k.

import random
import os

k = int(input("Enter the natural power of the number: "))
arr = []
for k in range(k):  
    arr.append(random.randint(0, 100))
print(arr)
print('{arr[0]}*x**{k} + {arr[1]}*x + {arr[2]} = 0')

road = r'file.txt'
with open(road, 'w') as f:
    f.write(('{arr[0]}*x**{k} + {arr[1]}*x + {arr[2]} = 0'))
