
my_list =['hello', '12', 'red', '567']
b = filter(str.isdigit, my_list)
for x in b:
    print(x, end=" ")    
