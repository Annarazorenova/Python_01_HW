# Напишите программу, которая принимает на вход вещественное
#  число и показывает сумму его цифр.

n = float(input('Enter a real number:  '))
# число в строку
str_n = str(n)
# замена десятичного разделителя
str_n = str_n.replace('.', '')
# строку с числом в список строк с числами
lst_str = list(str_n)
# преобразование в список целых чисел
lst_num = map(int, lst_str)
# функция sum
s = sum(lst_num)
print (s)