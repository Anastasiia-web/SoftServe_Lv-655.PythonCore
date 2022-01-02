## https://smartiqa.ru/python-workbook/bool
# # В чем разница между выражениями: True == 1 и True is 1? 

## Когда мы пишем True == 1, то сравниваем значения.
## Когда задается выражение True is 1, то сравниваются адреса в памяти.
## адреса через id() !!!
# True == 1
# True
# True is 1 # Сравниваются ячейки памяти
# False
# id(True), id(1)
# (2078150976, 2078275504) # Как видим – разные адреса в памяти


## Напишите функцию dislike_6(a), которая всегда возвращает True, если только 
# не передается число 6 типа int или типа float 
# (в данном случае она вернет «Только не 6!»).

def dislike_6(a):
    if int(a) != 6:
        return True
    else:
        return '«Только не 6!»'
print(dislike_6(6.009))   # «Только не 6!»

def dislike_6(a):
    if (type(a) is float or type(a) is int) and a == 6.0:
        return 'Только не 6!'
    return True

print(dislike_6('dffjg'))

## LISTs
d = ['f', 'h', 6, 4]
# if 4 in d:
#     print("Yes")
# else:
#     print("no")

# if 4 in d:
#     print(d.count(4))
# else:
#     print("no")

# print("Yes") if 4 in d else print(7)  # тернарный оператор

## 3. Чем отличаются методы append() и extend()?

lst = [1, 2, 3, 14, 33, 1, 1]
lst.extend('Добавка')
print(lst)   ## [1, 2, 3, 14, 33, 1, 1, 'Д', 'о', 'б', 'а', 'в', 'к', 'а']

lst = [1, 2, 3, 14, 33, 1, 1]
lst.append('Добавка')
print(lst)    ## [1, 2, 3, 14, 33, 1, 1, 'Добавка']

h = [1, 2, 3, 14, 33, 1, 9]   
# новый список начиная с элемента с индексом 2 (в нашем случае это цифра 3)
# вплоть до 6 элемента (не включая его) с шагом 2 (пропускаем каждое второе значение).
print(h[slice(2, 6, 2)])   # [3, 33]

w = [1, 2, 3, 14, 33, 1, 9]
f = w[slice(0,3,2)]    # [1, 3]
print(f)

h = [1, 2, 3, 14, 33, 1, 9]
print(h[2:6:2])   ## [3, 33]
print(h[::2])     ##  [1, 3, 33, 9]

w = [1, 2, 3, 14, 33, 1, 9]
print(w[::3])   #  [1, 14, 9]

## 6*. Какие способы создания списка из символов строки вы знаете?
f = 'python language'
# Option 1
print(list(f)) # ['p', 'y', 't', 'h', 'o', 'n', ' ', 'l', 'a', 'n', 'g', 'u', 'a', 'g', 'e']
print(f.split())   # ['python', 'language']
# Option 2
d = [i for i in f]   # ['p', 'y', 't', 'h', 'o', 'n', ' ', 'l', 'a', 'n', 'g', 'u', 'a', 'g', 'e']
print(d) 
# Option 3
e = []
for i in f:
    e.append(i)
print(e)             # ['p', 'y', 't', 'h', 'o', 'n', ' ', 'l', 'a', 'n', 'g', 'u', 'a', 'g', 'e']

## Дан произвольный список. Представьте его в обратном порядке.
w = [1, 2, 3]
# Option 1
w.reverse()
print(w)
# Option 2
x = [1, 2, 3]
print(x[::-1])    # список не поменяется!!!

## Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент. 
# В исходном списке минимум 2 элемента.

x = [1, 2, 3]
print(x[0])  # 1
print(x[-1])   # 3
print(x[1:-1]) # [2]
b = [x[-1], x[1:-1], x[0]]  # [3, [2], 1]
print(b)   # 3 [2] 1

my_list = [['f', 'h'], ['d'], [4,5]]   ## если все списки внутри!!! через sum
united_list = sum(my_list, [])        ## ['f', 'h', 'd', 4, 5]
print(united_list)
# def change(lst):
n = x.pop()   # [1, 2]
print(n)
print(x)
x.append(x[0])  # [1, 2, 1]
print(x)
print(x.pop(0))  # 1
x.insert(0, 7)    # [7, 2, 1]
print(x)

## Option 1 : методами pop() и insert().
def change(lst):
    new_start = lst.pop()  # Удаляем последний элемент и сохраняем его в переменную
    new_end = lst.pop(0)  # Удаляем первый элемент и сохраняем его в переменную
    lst.append(new_end)  # Добавляем к списку новый последний элемент
    lst.insert(0, new_start)  # Добавляем к списку новый первый элемент
    return lst
 
# Тесты
print(change([1, 2, 3]))             # [3, 2, 1]
print(change([1, 2, 3, 4, 5]))       # [5, 2, 3, 4, 1]
print(change(['н', 'л', 'о', 'с']))  # ['с', 'л', 'о', 'н']

#  Option 2 !!!
def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

# Тесты
print(change([1, 2, 3]))
print(change([1, 2, 3, 4, 5]))
print(change(['н', 'л', 'о', 'с']))

#+++++++++
a, b = 0, 1               # Fibinaci
while b <=5:
    print(b)
    a, b = b, a+b
#++++++====
#   # факториал Факториал числа — 
# #это произведение натуральных чисел от 1 до самого числа (включая данное число).
number = 5
fact = 1
while number >0:
    fact = fact *number
    number= number-1
print(fact)  # 120
# ++========

## Функция to_list() принимает неограниченное количество параметров. 
# Обработайте их так, чтобы на выходе получить список из этих элементов.

def to_list(*args):
    return list(args)
# Тесты
print(to_list(1, 5, 77))
print(to_list('Молоко', 5, '2020 год'))
print(to_list([3, 4, 7], 8.3, True, 'Строка'))

## Николай задумался о поиске «бесполезного» числа на основании списка. 
## Суть в следующем: он берет произвольный список чисел, находит самое большое из них, 
## а затем делит его на длину списка. 
## Студент пока не придумал, где может пригодиться подобное значение, но ищет у вас помощи 
## в реализации такой функции useless(s).
w = [1, 2, 3, 14, 33, 1, 9]
print(f'Max:  {max(w)}')      # Max:  33
## ИЛИ в обход ;)
w.sort()              # sort
print(w)
r = w.pop()           # find the biggest
print(r)
print(len(w))         # 6 + 1 (poped)
res = r/(len(w) + 1)
print(res)            # 4.714285714285714
print(round(res,2))   # 4.71

def useless(s):
    s.sort()
    i = s.pop()
    o = len(s)
    res = i / (o + 1)
    return round(res, 2)

print(useless([1, 5, 77]))
print(useless([19, 8.3, -4, 11, 0, 5]))
print(useless([-33, -0.05, -4.18, 11.2, 13.12, 55, 7.1]))

# Option 2
def useless(lst):
    return max(lst) / len(lst)

# ++++++
# Требуется создать функцию list_sort(lst), которая сортирует список чисел по убыванию их абсолютного значения.

def list_sort(lst):
    lst.sort()
    lst.reverse()
    return lst
print(list_sort([19, 8.3, -4, 11, 0, 5]))
# Option 2
def list_sort(lst):
    lst.sort(key=lambda x: abs(x), reverse=True)
    return lst


# На входе имеем список строк разной длины. 
# Необходимо написать функцию all_eq(lst), которая вернет новый список из строк одинаковой длины. 
# Длину итоговой строки определяем исходя из самой большой из них. 
# Если конкретная строка короче самой длинной, дополнить ее нижними подчеркиваниями с правого края 
# до требуемого количества символов.
# Расположение элементов начального списка не менять.

def all_eq(lst):
    max_item = max(lst, key=lambda x: len(x))
    max_len = len(max_item)
    return [item.ljust(max_len, '_') for item in lst]

# Тесты
print(all_eq(['крот', 'белка', 'выхухоль']))

# l = ['Молоко', 'j', '2020 год']
# for i in l:
#     print(len(i))



