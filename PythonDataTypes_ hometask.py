# TASK 1
'Flat is better than nested.'                                          # Записати стрічку з філософії Пайтона
         
print('Flat is better than nested.'.count('better'))                   # Знайти в заданій стрічці кількість входжень слів (better, never, is)
print('Flat is better than nested.'.count('never'))                    # Знайти в заданій стрічці кількість входжень слів (better, never, is)
print('Flat is better than nested.'.count('is'))                       # Знайти в заданій стрічці кількість входжень слів (better, never, is)
print('Flat is better than nested.'.upper())                           # Вивести весь текст у верхньому регістрі (всі великі літери)
print('Flat is better than nested.'.replace('i','&'))                  # Замінити всі входження символу “і” на “&”

# TASK 2
n = 1234                                                               # Задано чотирицифрове натуральне число
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

# Записати число в реверсному порядку
# Option 1
reverse_number = digit_4, digit_3, digit_2, digit_1

s = str(reverse_number)
d = eval(s)
print(d)
print('hi')


# DRAFTS
d=set('1234')

d=list('1234')
d.append(2)
print(d)

c= eval('3+5')  # конвертация str into int !!!
print(c)        # 8
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