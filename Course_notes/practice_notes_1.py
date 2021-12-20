##  https://chel-center.ru/python-yfc/2021/05/06/sintaksis-python-nbsp-mdash-bolshaya-shpargalka/
a =[]
i = 0
while i < 5:
    a.append(i)
    i += 1

print(list(a))

spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1
    break

while True:
    print('Please type your name.')
    name = input("Name? : ")
    if name == 'A':
        break
print('Thank you!')

while True:
    print('Please type your name.')
    name = input("Name? : ")
    if name == 'A':
        break
    else:
        continue
print('Thank you!')

w = [3,4,6]

for i in range(len(w)):   # первонач лист + умноженные на 2 ИНДЕКСЫ с 0 по 4  !!!
    w.append(i *2)
print(w)

for i in range(5):
    print('Джимми пять раз ({})'.format(str(i)))

q = []
for i in range(0, 10, 2):        # выведет только чётные числа Функция range() может иметь три аргумента. 
    print(i)                     # Значения первых двух аргументов start и stop, а третий аргумент — step.
    q.append(i)
print(q)

for i in range(5, -1, -1):       # обратный список через range(5, -1, -1) 
    print(i)                     # Для обратного отсчета можно использовать отрицательное значение параметра step !!!

import random

for i in range(5):
    print(random.randint(1, 10))   # 

# Обработка исключений

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError as e:
        print('Error: Invalid argument: {}'.format(e))

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

# List
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam)      # ['cat', 'bat', 'rat', 'elephant']
print(spam[0])   # 'cat'

print('The {} is afraid of the {}.'.format(spam[-1], spam[-3])) # 'The elephant is afraid of the bat.'

print(spam[1:])            # ['bat', 'rat', 'elephant']  # Получение фрагментов списков

# Удаление элементов списка, используя del
del spam[2]

# Использование цикла for для списков
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
# for i, supply in enumerate(supplies):
#     print('Index {} in supplies is: {}'.format(str(i), supply))

# OUTCOME: Index 0 in supplies is: pens
# OUTCOME: Index 1 in supplies is: staplers
# OUTCOME: Index 2 in supplies is: flame-throwers
# OUTCOME: Index 3 in supplies is: binders

# enumerate - for indexing in list  
s = list(enumerate(supplies))        # [(0, 'pens'), (1, 'staplers'), (2, 'flame-throwers'), (3, 'binders')]
print(s)

# after enumerate can be dictionary made !!!
t = dict(enumerate(supplies))        # {0: 'pens', 1: 'staplers', 2: 'flame-throwers', 3: 'binders'}
print(t)

# zip  - unites 2 lists  !!!
name = ['Pete', 'John', 'Elizabeth']
age = [6, 23, 44]
for n, a in zip(name, age):
    print('{} is {} years old'.format(n, a))

# OUTCOME:    Pete is 6 years old
# OUTCOME:    John is 23 years old
# OUTCOME:    Elizabeth is 44 years old

'howdy' in ['hello', 'hi', 'howdy', 'heyas']       # True
'h' not in ['hello', 'hi', 'howdy', 'heyas']       # True
'ho' in ['hello', 'hi', 'howdy', 'heyas']          # False

a, b = 'Alice', 'Bob'         # меняем списки-значения    
a, b = b, a
print(a)     # 'Bob'

# Метод index() для поиска значение в списке

spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
spam.index('Pooka')    # 1


# insert into list using index

spam = ['cat', 'dog', 'cat', 'bat']
spam.insert(1, 'chicken')
print(spam)                                  # ['cat', 'chicken', 'dog', 'bat']


a = spam.remove('cat')            # remove  уберёт только 1 раз !!!
print(spam)

for i in spam:                      # поэтому нужен цикл for !!! чтобы удалить всё !!!
    spam.remove("cat")
print(spam)

sort() списков    sorted() - новый список !!!

spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()    # ['ants', 'badgers', 'cats', 'dogs', 'elephants']

spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
sorted(spam)                 # ['ants', 'badgers', 'cats', 'dogs', 'elephants']   

d = list(spam[0])   
r = list(spam[1])
t = list(spam[2])
s = d + r + t                       # объединение списков черех + !!!      через , nested list !!!
       
print(spam[0])
print(d)
print(s)

# Словари и структуры данных

myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

## Методы keys(), values()
spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)
## red
## 42

for k in spam.keys():
    print(k)
## color
## age

print(spam)  # {'color': 'red', 'age': 42}

for i in spam.items():
    print(i)
## ('color', 'red')
## ('age', 42)

## Проверка наличия ключа или значения в словаре: in not in    получим     True / False    для ключей просто

print(42 in spam.values())        #  для values нужно values()

# Объединение двух словарей :  {**x, **y}

x = {'a': 1, 'b': 2}
y = {'c': 3, 'd': 4}
r = {**x, **y}

print(r)                  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# zip объединяет списки !!! мешая значения парами !!!
x = ['a', 1, 'b', 2]
y = [7, 4]
z = list(zip(x,y))
print(z)          # [('a', 7), (1, 4)]

# Set неупорядоченная коллекция элементов с уникальными значениями.
№ Наиболее эффективно for устранении дубликатов.

import collections


d = ['f', 'f', 8]
s = set(d)
f = list(s)
print(s)      # {8, 'f'}
print(f)      # [8, 'f']

## подробно про работу с  set (набором) посередине
#№ https://chel-center.ru/python-yfc/2021/05/06/sintaksis-python-nbsp-mdash-bolshaya-shpargalka/

# # Comprehensions
a = [1, 3, 5, 7, 9, 11]
[i - 1 for i in a]    # [0, 2, 4, 6, 8, 10]

b = {"abc", "def"}
{s.upper() for s in b}  # {"ABC", "DEF}

a = 'sdf jklk'                      # каждое слово с большой буквы 
print(a.title())                    # Sdf Jklk

## подробно о методах для строк in the middle
## https://chel-center.ru/python-yfc/2021/05/06/sintaksis-python-nbsp-mdash-bolshaya-shpargalka/

## Методы join() и split() для строк !!!

## strip() для строк !!! для удаления пробелов, а можно удалить ненужное strip('ghjk')

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))

## Регулярные выражения
import re

phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')   # \d = digits  # Создание объекта Regex функцией re.compile(). (Rcodecodeber to use a raw string.)
mo = phone_num_regex.search('My number is 415-555-4242.')   # search чтобы помечить
print('Phone number found: {}'.format(mo.group()))   # Phone number found: 415-555-4242 
#метод group() объекта Match для возврата строки фактического сопоставленного текста.

u= 'ghj6'
# f = u.remove('\d')
print(u.find('\d'))   # -1  возвращает индекс где цифра

# ## Группировка в круглые скобки задаётся в compile() методе

phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_num_regex.search('My number is 415-555-4242.')
mo.group(1)
'415'
mo.group(2)
'555-4242'
mo.group(0)
'415-555-4242'
mo.group()
'415-555-4242'

# ##  используйте метод groups() — обратите внимание на форму множественного числа для имени
mo.groups()
('415', '555-4242')
area_code, main_number = mo.groups()
print(area_code)
415
print(main_number)
555-4242

## Знак * (называемый звездой или звездочкой) означает «совпадение ноль или более» — группа,
## предшествующая звездочке, может встречаться в тексте любое количество раз.

s ='hjkk4'
ss = s.rfind(r'\d')
print(ss)
p = s.strip('4')   # удалили из строки символ
print(p)

k = list(s)
l = k.pop()   # вернёт 4 и удалит
print(''.join(k))    # вернёт строку обрезанную обратно


## Метод findall() 
##  В то время как search() вернет объект Match первого совпадающего текста в искомой строке,
# # метод findall() вернет строки каждого совпадения в искомой строке.

phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
phone_num_regex.findall('Cell: 415-555-9999 Work: 212-555-0000')   # ['415-555-9999', '212-555-0000']

# ## создание моего класса для поиска по регулярке !!!
vowel_regex = re.compile(r'[aeiouAEIOU]')
vowel_regex.findall('Robocop eats baby food. BABY FOOD.') # ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']

# ## Поместив символ вставки (^) сразу после открывающей скобки класса символов, можно создать отрицательный класс символов.
# ## Отрицательный класс символов будет соответствовать всем символам, не входящим в этот класс символов. 
# consonant_regex = re.compile(r'[^aeiouAEIOU]')
# consonant_regex.findall('Robocop eats baby food. BABY FOOD.')
['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', '
', 'B', 'B', 'Y', ' ', 'F', 'D', '.']

## вы можете использовать ^ и $ вместе, чтобы указать, что вся строка должна соответствовать регулярному выражению
## https://chel-center.ru/python-yfc/2021/05/06/sintaksis-python-nbsp-mdash-bolshaya-shpargalka/

i = re.compile(r'\d')

s = i.findall('hj7 8')
print(s)    # ['7', '8']


(lambda x, y: x + y)(5, 3)

add = lambda x, y: x + y
add(5, 3)

## __main__ is the name of the scope in which top-level code executes.
# #A module’s name is set equal to __main__ when read from standard input, a script, or from an interactive prompt.

# #A module can discover whether or not it is running in the main scope by checking its own __name__, which allows 
# #a common idiom 
# #for conditionally executing code in a module when it is run as a script or with python -m but not when it is imported:
# # if __name__ == "__main__":
## execute only if run as a script in main file 

## Advantages   ↑
## Every Python module has it’s __name__ defined and if this is __main__, it implies that the module is being 
## run standalone by the user and we can do corresponding appropriate actions.
## If you import this script as a module in another script, the name is set to the name of the script/module.
## Python files can act as either reusable modules, or as standalone programs.
# #if __name__ == “main”: is used to execute some code only if the file was run directly, and not imported.

### Virtual Environment and setup at the end of
## https://chel-center.ru/python-yfc/2021/05/06/sintaksis-python-nbsp-mdash-bolshaya-shpargalka/

