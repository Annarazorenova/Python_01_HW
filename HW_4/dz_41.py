# Вычислить число c заданной точностью d
# Пример:
#  при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# from math import pi
# d = int(input('Enter accuracy of calculating: '))
# print(*{round (pi, d)})
d = int(input('Enter accuracy of calculating:'))
pi = 0
for n in range(d):
    pi += (1/16 ** n) * (4 / (8 * n + 1) - 2 / (8 * n + 4)
          - 1 / (8 * n + 5) - 1 / (8 * n + 6))
print( 'Число ПИ: ' , round(pi, d))    