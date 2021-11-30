# TASK 1
'Flat is better than nested.'                                          # Записати стрічку з філософії Пайтона
         
print('Flat is better than nested.'.count('better'))                   # Знайти в заданій стрічці кількість входжень слів (better, never, is)
print('Flat is better than nested.'.count('never'))                    # Знайти в заданій стрічці кількість входжень слів (better, never, is)
print('Flat is better than nested.'.count('is'))                       # Знайти в заданій стрічці кількість входжень слів (better, never, is)
print('Flat is better than nested.'.upper())                           # Вивести весь текст у верхньому регістрі (всі великі літери)
print('Flat is better than nested.'.replace('i','&'))                  # Замінити всі входження символу “і” на “&”

# TASK 2
n = 1230                                                               # Задано чотирицифрове натуральне число
print(n)

# 1. Знайти добуток цифр цього числа
digit_1 = int(n/1000)
digit_2 = int(n/100)%10
digit_3 = int(n/10)%(int(n/100))
digit_4 = n%(int(n/10))                                                

digits_multiplication = int(n/1000) * (int(n/100)%10) * (int(n/10)%(int(n/100))) * (n%(int(n/10)))

print(digits_multiplication)
print(digit_1)
print(digit_2)
print(digit_3)
print(digit_4)

# 2. Записати число в реверсному порядку
# Option 1
print(digit_4,digit_3,digit_2,digit_1)     # ? There are spaces in between digits. How to get rid of them?

# Option 2
reverse_number = digit_4, digit_3, digit_2, digit_1      # ? Is there a way how to join tuple?          
print(reverse_number)

# Option 3
input_number_for_reversing = input('What is a number to reverse? ')
reversed_number = input_number_for_reversing[::-1]

print('Reversed number is', reversed_number)

# Option 4

n = 900         # ? Цикл обрежет нули. Как этого избежать?
m = 0
while n>0:
    m = m*10 + n%10
    n = n//10
print(m)

# Option 5
n1 = input("Введите целое число: ")        # n2 - строка, как корректно перевести в число?
n_list = list(n1)
print(n_list)           #['6','7']
n_list.reverse()
n2 = "".join(n_list)
print('"Обратное" ему число:', n2)

# Option 6
n1 = input("Введите целое число: ") 
n2 = n1[::-1] 
print('"Обратное" ему число:', n2)

# Option 7
k='500'                                    # result - строка, как корректно перевести в число?
result = ""
for i in reversed(k): 
    result += i
print(result)

# Option 8
s='900'                                    # result1 - строка, как корректно перевести в число?
result1=""
for i in range(len(s)-1, -1, -1):
    result1 += s[i]
print(result1)

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

# Draft demo
a = 3; b = 2; # [3; 2]
a *= b;       # [6; 2]
b /= a;       # [6; 3]
a /= b;       # [2; 3]

# DRAFTS
#d=set('1234')

#d=list('1234')
#d.append(2)
#print(d)

#c= eval('3+5')  # конвертация str into int !!!
#print(c)        # 8
# type(c)         #   <class 'int'>
# import this
#The Zen of Python, by Tim Peters   

#Beautiful is better than ugly.     
#Explicit is better than implicit.  
#Simple is better than complex.     
#Complex is better than complicated.
#Flat is better than nested.        
#Sparse is better than dense.       
#Readability counts.
#Special cases aren't special enough to break the rules.
#Although practicality beats purity.
#Errors should never pass silently.
#Unless explicitly silenced.
#In the face of ambiguity, refuse the temptation to guess.
#There should be one-- and preferably only one --obvious way to do it.
#Although that way may not be obvious at first unless you're Dutch.
#Now is better than never.
#Although never is often better than *right* now.
#If the implementation is hard to explain, it's a bad idea.
#If the implementation is easy to explain, it may be a good idea.
#Namespaces are one honking great idea -- let's do more of those!


# http://www.kievoit.ippo.kubg.edu.ua/kievoit/2016/73_Python/index.html string methods
# https://tproger.ru/translations/python-sorting/
# https://itisgood.ru/2021/04/15/kak-pomenjat-mestami-dve-peremennye-v-python/