from functools import reduce
digits =list(map(int, ['1', '3', '8', '6', '9', '2']))
# print(digits)
sum_A = reduce(lambda a, b: a + b, digits[1::2])
print(sum_A)