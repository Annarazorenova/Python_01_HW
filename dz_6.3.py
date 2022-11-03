n = int(input('Enter a number: '))
lst = [(1 + 1 / i) ** i for i in range(1, n + 1)]
print(sum(lst))
