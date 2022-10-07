# Задайте список из n чисел последовательности
# (1 + 1 / n)^n и выведите на экран их сумму.

n = int(input('Enter number: '))
list = []
sum = 0
for i in range(1, n+1):   
    num = (1 + 1 / i)**i    
    list.append('{0: .4}'.format(num)) 
    sum += num

print('Summa: ', '{0: .4}'.format(sum) )   