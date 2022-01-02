## https://smartiqa.ru/python-workbook ТЕОРИЯ, ВОПРОСЫ, ЗАДАЧИ, РЕШЕНИЯ
# 
# 
# https://tproger.ru/translations/python-sorting/
## sorted вернёт новый по возрастанию   - со всеми итерируемыми объектами
## list.sort() изменент старый список   - только для списков

##  Filter list
t = ['d', 5, 'g', 9]
## Numbers
d = [4, 5, 7, 9]
f = [x for x in d if x%2==1] ## отбрали нечётные и посчитали (len)
p = {'odd': len(f)}  
print(p)  ## {'odd': 3}


t = ['d', 5, 'g', 9]
h = t.__len__()  ## 4
print(h)

## Отфильтровать цифры от бувк в списке
t = ['d', 5, 'g', 9]
# u = [i for i in t if i.isdigit()]
u = [str(i) for i in t]   # ['d', '5', 'g', '9']
print(u)   
e = [i for i in u if i.isdigit()]    # ['5', '9']
print([int(i) for i in e])   # [5, 9]



## из строки вывести числа
str = "h3110 23 cat 444.4 rabbit 11 2 dog"
x = [int(s) for s in str.split() if s.isdigit()]  ## [23, 11, 2]  ## split() разбивает по словам строку !!!
print(x)

d = "fajj8njn3nbl"
p = list(d)    ## list() разбивает по элементам !!!
print(p)   ## ['f', 'a', 'j', 'j', '8', 'n', 'j', 'n', '3', 'n', 'b', 'l']
r = [i for i in p if i.isdigit()]
print(r)   ## ['8', '3']


# >>> student_tuples = [
#         ('john', 'A', 15),
#         ('jane', 'B', 12),
#         ('dave', 'B', 10),
#     ]
# >>> sorted(student_tuples, key=lambda student: student[2])   # сортируем по возрасту
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

# >>> class Student:
#         def __init__(self, name, grade, age):
#             self.name = name
#             self.grade = grade
#             self.age = age
#         def __repr__(self):
#             return repr((self.name, self.grade, self.age))
#         def weighted_grade(self):
#             return 'CBA'.index(self.grade) / self.age

# >>> student_objects = [
#         Student('john', 'A', 15),
#         Student('jane', 'B', 12),
#         Student('dave', 'B', 10),
#     ]
# >>> sorted(student_objects, key=lambda student: student.age)   # сортируем по возрасту
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

## убираем симводы из строк https://evileg.com/uk/post/642/   str.replace("$", "")  str.replace("$", "", 20)
## Option 1
s="Hello$ Python3$"
s1=s.replace("$", "")  ## Hello Python3
print (s1)

s="Hello$ Python3$"
s1=s.replace("$", "", 1)  ## Hello Python3$
print (s1)

s="Hello$ Python3$"
s1=s.replace("$", "", 20)  ## Hello Python3
print (s1)
## Option 2      re.sub()
import math
import re
s="Hello$@& Python3$"
s1=re.sub("[$|@|&]","",s)  ##  Hello Python3
print (s1)

# https://evileg.com/uk/post/642/
# 1. За допомогою 'isalpha()'
# 2. За допомогою 'filter()'
# 3. За допомогою 're.sub()'

# Фильтруем буквы
input_1 = list('gfhjh67j')
## Option 1
d ="".join([i for i in input_1 if i.isalpha()])
print(d)

## Фильтруем цифры 
## Опция через функцию
def l():
    y = []
    for i in input_1:
        if i.isdigit():
            y.append(i)
    print(''.join(y))
l()
## Option 3
k = "iph77"
import re      ## Фильтруем через 
valids = re.sub(r"[^A-Za-z]+", '',k)   ## iph
print(valids)

## Флаг re.I игнорирует регистр, поэтому также заменяются строчные символы ( a-z ).

import re
myString = 'hj7887vgv'
def charFilter():
    return re.sub('[^A-Z]+', '', myString, 0, re.I)  ## hjvgv
print(charFilter())

## Option 4
output = ''
for character in input_1:
    if character.isalpha():
        output += character
print(output)      ### gfhjhj

# import math
# k = math.floor(7.5)    # 7 !!!
# print(k)

## https://smartiqa.ru/python-workbook/int#1
## Задачи Python
## 1

# v = 11 * 2 ** 2 - 13 / 4 + 7

# print(v)   # 47.75

## Сначала по приоритету возводим в степень (2 ** 2). Далее умножаем (11 * 4). 
# Потом делим (13 / 4). Следом вычитаем (44 - 3.25). На последнем этапе применяем сложение (40.75 + 7). 
# Получаем число с плавающей точкой 47.75. Если привести его к типу int, то результат равняется 47.

## 
## 2
# print(3 ** 9090001)
# Сколько мегабайт памяти занимает число 3 ** 9090001? 
# Для решения воспользуйтесь функцией getsizeof() из модуля sys.
## Не торопитесь. Придется подождать около 10 секунд на вычисление выражения 
# (в зависимости от мощности компьютера). Как известно, в одном килобайте – 1024 байт, 
# а в одном мегабайте – 1024 Кб. Для вычисления объема занимаемой памяти воспользуемся функцией 
# getsizeof() из модуля sys. 
# Получим: sys.getsizeof(3 ** 9090001) / (1024 * 1024) = 1.83 Мб приблизительно.
# 1. Импортируем функцию из модуля
from sys import getsizeof
# 2. Находим объем занимаемом памяти в Мегабайтах
# print(getsizeof(3 ** 9090001) / (1024 * 1024))   ## 1.8320083618164062
# Результат: 1.8319969177246094

## 3
# Используя стандартные арифметические операции представьте самое 
# большое целое число из цифр 4, 4, 4 и приведите его значение.
# Операция возведения в степень дает невероятно большое число, значение которого больше, 
# чем атомов в известной Вселенной.

# print(4 ** 4 ** 4) # 134078079299425970995740249982058461274793658205923933777235614437217640300
# 73546976801874298166903427690031858186486050853753882811946569946433649006084096

## 4
## Напишите функцию pos_add(a, b), которая возвращает положительное значение сложения двух целых чисел.
## Оптимальный вариант – использовать встроенную функцию abs(), которая возвращает положительное число.
def pos_add(a, b):
   return abs(a + b)

## 5 
## Определите функцию foo(a), которая возвращает результат целочисленного и 
# по модулю деления любого целого числа на -11.
# Целочисленное деление – результат выполнения операции «//», а делению по модулю – операции «%». 
# a = int(input(": "))
# def foo():
#     return a//-11, a%-11
# print(foo())   ## для 22 это (-2, 0)

## 6
## Напишите функцию num_sum(a), принимающую любое значение. 
# Если это целое число, то возвратить сумму его чисел. 
# В противном случае возвращается фраза «Это не целое число».

# def num_sum(a):
#    # 1. Определяем принадлежность значения 'a' к целому числу, но не к булеву типу
#    if isinstance(a, int) and not isinstance(a, bool):
#        # 2. Преобразуем число в положительное, а потом - строку
#        a_to_str = str(abs(a))
#        # 3. Задаем начальную сумму 0
#        s = 0
#        # 4. В цикле складываем все числа
#        for i in a_to_str:
#            s += int(i)
#        return s
#    return 'Это не целое число'

# # Тесты
# print(num_sum(-146))
# print(num_sum('-11'))
# print(num_sum(True))
def num_sum(a):
    if isinstance(a, int):
        a = list()
        s = 0
        for i in a:
            s +=i
            print(s)
    else:
        print('Это не целое число')

# Тесты
num_sum(-146)
# print(num_sum('-11'))
# print(num_sum(True))

## РЕШЕНИЕ 
b = 123
v = b%10   # 3  !!! отделяем последнее число !!! чурез % 10   ## https://younglinux.info/python/task/sum-mult
print(v)
y = b% 100 //10
print(y)   ## 2
x = b%1000 //100   ## 1
print(x)
suma = b%10 + b% 100 //10 + b%1000 //100
print(suma)
## Через цикл !!!! объяснение   https://younglinux.info/python/task/sum-mult
n = 1234
suma = 0
while n > 0:
    digit = n % 10
    suma = suma + digit
    n = n // 10
print("Сумма:", suma)

## Через цикл !!!! объяснение   https://younglinux.info/python/task/sum-mult
nu = 425
mult = 1
while nu > 0:
    digit = nu % 10
    mult = mult * digit
    nu = nu // 10
print("Произведение:", mult)

######
# Изменение значений переменных можно записать в сокращенном виде:
while n > 0:
    digit = n % 10
    suma += digit
    mult *= digit
    n //= 10
#########     разобраться их ответ из https://smartiqa.ru/python-workbook/int#1 !!!

# def num_sum(a):
#    # 1. Определяем принадлежность значения 'a' к целому числу, но не к булеву типу
#    if isinstance(a, int) and not isinstance(a, bool):
#        # 2. Преобразуем число в положительное, а потом - строку
#        a_to_str = str(abs(a))
#        # 3. Задаем начальную сумму 0
#        s = 0
#        # 4. В цикле складываем все числа
#        for i in a_to_str:
#            s += int(i)
#        return s
#    return 'Это не целое число'

# # Тесты
# print(num_sum(-146))
# print(num_sum('-11'))
# print(num_sum(True))

#######

## 7
# Дана последовательность случайных цифр любой длины и «волшебное» положительное число, больше нуля. 
# Напишите функцию magic(), принимающую эти аргументы, и выясните, можно ли разделить 
# сумму квадратов последовательности на «волшебное» число без остатка. 
# В качестве ответа возвращается «Волшебство случается» в случае успеха или «Никакого волшебства», 
# если разделить нельзя.

v = 5
d = 6
w = 2

def c():
    if (v**2 + d**2)%w == 0:
        print('«Волшебство случается»')
    else:
        print('«Никакого волшебства»')
c()

###
def magic(*args, k):
   sq_sum = 0              # 1. Начальная сумма равна нулю
   for i in args:          # 2. Складываем квадраты всех аргументов в цикле
       sq_sum += i ** 2
   if sq_sum % k == 0:     # 3. Определяем, равен ли остаток от деления sq_sum на k нулю
       return 'Волшебство случается'
   return 'Никакого волшебства'

# Тесты
print(magic(2, 5, 7, k=5))
print(magic(2, 5, 7, k=39))
print(magic(2, 5, 7, k=2))

####
print(isinstance(4, int))   ##  узнать тип # True
print((4.0).is_integer())  ## ##  узнать тип # True

## https://smartiqa.ru/python-workbook/float  ОКРУГЛЕНИЕ В ПАЙТОН !!!

## В языке Python используется так называемое банковское округление 
# (на основании стандарта IEEE 754). Его суть в следующем: округление числа 
# производится в сторону ближайшего значения, а если последняя цифра 5, 
# то в сторону ближайшего четного числа.

# Примеры – Интерактивный режим
# >>> round(2.3)
# 2
# >>> round(2.8)
# 3
# >>> round(-2.8)
# -3
# >>> round(2.5)
# 2
# >>> round(3.5)
# 4
## Дано 4 числа. 

# Task 1 FLOAT   https://smartiqa.ru/python-workbook/float#1
# Нужно написать функцию avg_5(a, b, c, d), которая 
# возвращает среднее арифметическое аргументов и округляет его до 5 знаков после запятой.

def avg_5(a, b, r, d):
    return round(((a + b + r + d)/4), 5)

print(avg_5(1.987635,2,3,4))  # 2.74691

# Task 3 https://smartiqa.ru/python-workbook/float#1

## Функция mul_to_int(a, b) может принимать целые или вещественные числа. 
# Если результат умножения аргументов не имеет значимых чисел после запятой, 
# то она возвращает его в виде целого числа. 
# В противном случае – в виде float. 

def mul_to_int(a, b):
    res = a * b
    if float(res).is_integer():
        return int(res)
    return res
print(mul_to_int(3.0008, 5))  # 15.004






