# Task 3
# Посортувати цифри, що входять в дане число
input_number_to_sort = input('What is a number to sort? ')
ready = sorted(input_number_to_sort)        # ? Как собрать сортированный список в число ?
print('Sorted number: ', ready)   

# Task 4
# Поміняти між собою значення двох змінних, не використовуючи третьої змінної
# Option 1
g = 7
j = 700
g,j = j,g
print(g)     #output 700
print(j)     #output 7

# Option 2
# Использование комбинации сложения и вычитания
a = 10
b = 2
a = a + b    # a=10+2=12
b = a - b    # b=12-2=10
a = a - b    # a=12-10=2
print(a)
print(b)

# Option 3
# Использование комбинации умножения и деления
a = 100
b = 20
a = a*b     # a=10020=2000
b = a/b     # b=2000/20=100
a = a/b     # a=2000/100=20
print(int(a))
print(int(b))
