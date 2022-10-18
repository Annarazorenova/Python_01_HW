# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
def Prime_factors():
    n = int(input('Enter a natural number: '))
    i = 2
    arr = []
    while i <= n:
        if n % i == 0:
            arr.append(i)
            n //= i
        else:
            i += 1  
    print(arr)  
Prime_factors()            