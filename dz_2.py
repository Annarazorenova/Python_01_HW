# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('Введите число: '))
y = int(input('Введите число: '))
z = int(input('Введите число: '))

for x in [True,False]:
    for y in [True,False]:
        for z in [True,False]:
            print(x,'AND',y,'OR',z,'=',x and y or z)