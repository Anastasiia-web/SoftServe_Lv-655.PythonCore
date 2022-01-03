## https://smartiqa.ru/python-workbook/dict#1

## Task 1
## Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь, 
# в котором каждый элемент списка является и ключом и значением. 
# Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях. 

# def to_dict():                                                    ## working!!!!
#     return {element: element for element in words}
# print(to_dict())

## сортировка по ключу или значению !!!                        ### https://all-python.ru/osnovy/slovari.html

# Сортировка осуществляется за счет импортированного модуля operator 
# и встроенного метода itemgetter, получающего 0 или 1.

import operator                                                ### https://all-python.ru/osnovy/slovari.html

a = {2 : "two", 3 : "three", 1 : "one"}
b = sorted(a.items(), key = operator.itemgetter(0))  # [(1, 'one'), (2, 'two'), (3, 'three')]
print(b)
b = sorted(a.items(), key = operator.itemgetter(1))  # [(1, 'one'), (3, 'three'), (2, 'two')]
print(b)

## аргумент 0 позволяет отсортировать словарь по ключу, 
## аргумент 1 дает возможность вывести его содержимое в алфавитном порядке значений.

words = ["dan","kar","dream","adsadsadad","AHAHAHAHAHAHHHAAHAHA","aaa"]
# a = {a: a * a for a in range(len(words))}   # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# print(a)

a = {a: a * a for a in range(5)}
print(a)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

a = {a: 'h' for a in words}
print(a)   # #{'dan': 'h', 'kar': 'h', 'dream': 'h', 'adsadsadad': 'h', 'AHAHAHAHAHAHHHAAHAHA': 'h', 'aaa': 'h'}

print(a.get('aaa'))   # h   # доступ к значению по ключу
print(a.get('K4', 'Нет такого ключа')) # Нет такого ключа ЛУЧШЕ (с заглушкой если нет ключа)# доступ к значению по ключу
print(a.values())     # dict_values(['h', 'h', 'h', 'h', 'h', 'h'])
print(a.keys())       # dict_keys(['dan', 'kar', 'dream', 'adsadsadad', 'AHAHAHAHAHAHHHAAHAHA', 'aaa'])
print(a.items()) #dict_items([('dan', 'h'), ('kar', 'h'), ('dream', 'h'), ('adsadsadad', 'h'), 
#('AHAHAHAHAHAHHHAAHAHA', 'h'), ('aaa', 'h')])

wo = ["dan","kar","dream","adsadsadad","AHAHAHAHAHAHHHAAHAHA","aaa"]
s = {element: element for element in wo}
x = {a:a * a for a in range(7)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
print(x)
f = dict(zip(x,s))   # {0: 'dan', 1: 'kar', 2: 'dream', 3: 'adsadsadad', 4: 'AHAHAHAHAHAHHHAAHAHA', 5: 'aaa'}
print(f)

## update() dict
my_dict = {'first_one': 'we can do it'}

def biggest_dict(**kwargs):
    my_dict.update(**kwargs)

biggest_dict(k1=22, k2=31, k3=11, k4=91)
biggest_dict(name='Елена', age=31, weight=61, eyes_color='grey')
print(my_dict) ## {'first_one': 'we can do it', 'k1': 22, 'k2': 31, 'k3': 11, 'k4': 91, 
## 'name': 'Елена', 'age': 31, 'weight': 61, 'eyes_color': 'grey'}

g = {}
g = {'s': 6, 'k': 9} ## {'s': 6, 'k': 9}
g.update({'h':8})    ## {'s': 6, 'k': 9, 'h': 8}
g.update({'7':8})    ## {'s': 6, 'k': 9, 'h': 8, '7': 8}
print(g)

## Дана строка в виде случайной последовательности чисел от 0 до 9. 

# Требуется создать словарь, который в качестве ключей будет принимать данные числа 
# (т. е. ключи будут типом int), а в качестве значений – количество этих чисел в имеющейся 
# последовательности. Для построения словаря создайте функцию count_it(sequence), принимающую строку из цифр. 
# Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.
i = {}
# key = int(input(':? '))  # working !!!
# value = len(str(key))
# i.update({key:value})
# print(i)
# while len(i) < 4:           # working !!!
#     key = int(input(':? '))
#     value = len(str(key))
#     i.update({key:value})   # {87: 2, 567: 3, 987: 3, 6: 1}
# print(i)

## Option 2                                    # https://smartiqa.ru/python-workbook/dict#2

def count_it(sequence):
    # При помощи генератора создаем словарь, где ключом выступает уникальный элемент строки, 
    # а значением - его частота (вычисляется методом count()) 	
    num_frequency = {int(item): sequence.count(item) for item in sequence}

    # Сортируем словарь по значениям в порядке возрастания. Для этого методом items() формируем пары “(ключ, значение)” в виде кортежей по всем элементам словаря. Т. к. нужно сортировать по значениям, берем второй элемент кортежей. В результате получим список из кортежей “(ключ, значение)”
    sorted_num_frequency = sorted(num_frequency.items(), key=lambda element: element[1])

    # Возвращаем последние 3 элемента списка, т. е. кортежи с самыми большими значениями второй компоненты, которые преобразовываем в словарь 
    return dict(sorted_num_frequency[-3:])

# Тесты
print(count_it('1111111111222'))
print(count_it('123456789012133288776655353535353441111'))
print(count_it('007767757744331166554444'))

# OPtion 3      working !!!

q = '1111111111222'
f = {int(item): q.count(item) for item in q}
print(f)    # {1: 10, 2: 3}

## Option 4

from collections import Counter

def count_it(sequence):
    return dict(Counter([int(num) for num in sequence]).most_common(3))

# Тесты
print(count_it('1111111111222'))   # {1: 10, 2: 3}

# Создайте словарь с количеством элементов не менее 5-ти. 
# Поменяйте местами первый и последний элемент объекта. Удалите второй элемент. 
# Добавьте в конец ключ «new_key» со значением «new_value». 
# Выведите на печать итоговый словарь. Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).

t = {i: i * 3 for i in range(5)}   # {0: 0, 1: 3, 2: 6, 3: 9, 4: 12}
print(t)

# e = t
# print(e)            # {0: 0, 1: 3, 2: 6, 3: 9, 4: 12}
# y = t.popitem()   # {0: 0, 1: 3, 2: 6, 3: 9}
# print(t)
# print(y)          # (4, 12)
# t.update({y})     # {0: 0, 1: 3, 2: 6, 3: 9, 4: 12}
# print(t)
# t.update({'new key': 'new value'})     # {0: 0, 1: 3, 2: 6, 3: 9, 4: 12, 'new key': 'new value'}
# print(t)

y = list(t.keys())     # [0, 1, 2, 3, 4]          # делаем списки чтобы работать со значениями
x = list(t.values())        # [0, 3, 6, 9, 12]    # делаем списки чтобы работать со значениями
y[0], y[-1] = y[-1], y[0]   # [4, 1, 2, 3, 0]     # меняем местами 1 и последний элементы !!! список
x[0], x[-1] = x[-1], x[0]   # [12, 3, 6, 9, 0]    # меняем местами 1 и последний элементы !!! список
y.pop(1)                                          # удаляем второй элемент
x.pop(1)
t = dict(zip(y,x))                                
t.update({'new key': 'new value'})                # добавляем новые значения
print(t)


# p = x.remove(3)             # [12, 6, 9, 0]     # удаление элемента если его знаем remove()
# print(x)

# x.pop(1)                      # [12, 6, 9, 0]     # удаление элемента по индексу pop()
# print(x)

# Option 2

# >>> from collections import OrderedDict
# >>> dct = OrderedDict({1: 1, 2: 2, 3: 3, 4: 4, 5: 5})

# # Меняем местами первый и последний элементы
# >>> first = list(dct.items())[0]
# >>> last = list(dct.items())[-1]
# >>> dct.move_to_end(key=first[0])
# >>> dct.move_to_end(key=last[0], last=False)

# # Удаляем второй элемент
# >>> second = list(dct.items())[1]
# >>> del dct[second[0]]

# # Вставляем новый элемент
# >>> dct['new_key'] = 'new_value'
# >>> my_dict
# {5: 5, 3: 3, 4: 4, 1: 1, 'new_key': 'new_value'}
# >>> id(my_dict)
# 17128656
# >>> start_dict_id
# 17128656