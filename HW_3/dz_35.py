# Задайте число. Составьте список чисел Фибоначчи,
#  в том числе для отрицательных индексов.
k = int(input('Enter number: '))
a0 = 1
a1 = 1
c = 1
arr = []
for i in range(k):
    arr.append(a0)
    c = a1 + a0
    a0 = a1
    a1 = c
# print(arr) 
new_arr = arr[:]
for i in range(1,len(arr), 2):
    arr[i] = - arr[i]
    new_arr = new_arr[::-1]
    new_list =(new_arr[::-1] +[0] + arr)
print(new_list)

