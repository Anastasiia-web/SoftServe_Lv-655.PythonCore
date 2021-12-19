## https://proglib.io/p/50-python-projects  про библиотеки и их возможности

# https://proglib.io/p/python-tricks

# 1. Объединение списков без цикла

my_list = [['f', 'h'], ['d'], [4,5]]
united_list = sum(my_list, [])
print(united_list)


# 2. Обмен значениями при помощи кортежей

tuple_1, tuple_2 = ('g', 'p'), (4, 8)
new_tuple = tuple_2, tuple_1
print(new_tuple)

# перевод в лист чтобы чтобы что-то сделать с тюплом и потом в стрингу

list_out_of_tuple_1 = list(tuple_1)              # меняем местами
list_out_of_tuple_2 = list(tuple_2)
united_new_list = list(list_out_of_tuple_2 + list_out_of_tuple_1)          # объединяем
print(united_new_list)
str_list = [str(i) for i in united_new_list]      # каждое значение в стрингу
print(str_list)
str_out_of_list = "".join(str_list)          # в стрингу
print(str_out_of_list)


# for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]:
#     print(a, b, c)

# 3. Распаковывание последовательностей при неизвестном числе элементов

# 4. Объединение строк

a = ["Python", "-", "прекрасный", "язык."]
b = " ".join(a)
print(b)

c = b.split('-')
print(c)

numbers = [1, 2, 3, 4, 5]
print(', - '.join(map(str, numbers)))     # показываем как хотим объединить

# 6. Транспонирование двумерного массива данных
# Чтобы поменять местами строки и столбцы матрицы,
# созданной с помощью встроенных типов данных, воспользуйтесь функцией zip:

original = [('a', 'b'), ('c', 'd'), ('e', 'f')]
transposed = zip(*original)
print(list(transposed))

# Дикшинари из списка !!!

z = ['e', 'f']                    #    2 списка
y = [1, 2]

zy = y , z                        #    свела вместе
print(zy)

transposed_my = zip(*zy)          #  сводим вместе 2 списка через zip(*zy) !!!!! в новом списке: сп1, сп2, сп1, сп2
e = dict(transposed_my)           #  сделала список словарём !!!
print(e)

# _____________

n = list(range(4))
w = ['a', 'x', 'z', 0]

nw = n,w
ziped_nw = zip(*nw)
d_ziped_nw = dict(ziped_nw)
print(d_ziped_nw)

# тоже только короче !!! Дикшинари из списка !!!

shot_ziped_nw = dict(zip(*(n,w)))
print(shot_ziped_nw)

#___________________

# 7. Удаление дубликатов в списке
items = [2, 2, 3, 3, 1]
u = list(set(items))                      # просто удалит дубликаты и посортирует !!!

# !!! Cохранить порядок следования элементов.
# Для этого тип данных OrderedDict из модуля collections:

items = [2, 2, 3, 3, 1]

from collections import OrderedDict

print(list(OrderedDict.fromkeys(items).keys()))

#____________

o = list(sorted(items))              # сортируем без удаления дубликатов
print(o)

# 11. Вывод при помощи "print()"

# В print имеются следующие аргументы:

# строка "sep" (по умолчанию один пробел), вставляемая между объектами при выводе;
# строка "end" (по умолчанию \n), добавляемая в конец выводимого текста;
# file (по умолчанию sys.stdout) – любой объект, поддерживающий метод файлов write(string),
#  то есть стандартный поток, файл и др.
# Например, если нам не нужно объединять подстроки, а лишь напечатать суммарную строку:

for part in ["prog", "lib", ".io", "\n"]:
    print(part, end='')


g = ["an", "lib", ".com"]                       # проще) "".join(list_my)
print("".join(g))

# 12. Нумерованные списки
for i, item in enumerate(['a', 'b', 'c'], 1):
    pi = i, item  
    dict_m = {}                              # enumerate() !!! нумерует списки
    print(pi)

    # print(i, item)
    

# !!! enumerate у функции есть второй аргумент, задающий начальное число:

for i, item in enumerate(['a', 'b', 'c'], 1):
    m = i, item
    # print(i, item)

# 13. Сортировка словаря по значениям

d = {'яблоки':40, 'апельсины':80, 'бананы':70}
print(sorted(d, key=d.get))                        # outcome:  ['яблоки', 'бананы', 'апельсины']

# 14. Генераторы словарей и множеств

S = {i**2 for i in range(10)}       # outcome SET !!! for S:   {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
D = {i: i**2 for i in range(10)}    # outcome DICT !!! for D: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

print(S)
print(D.values())                   # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(D.keys())                     # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 15. Нахождение наиболее часто повторяющихся элементов списка   max, count

a = [1, 2, 3, 1, 2, 3, 2, 2, 4, 5, 1] 
print(max(set(a), key=a.count))


#____________

# My drafts

# # перевод в дикшинари

# my_list_2 = ['f', 'h', 'd', 4, 5]
# for_converting_to_list = [str(i) for i in my_list_2]
# str_2 = list("".join(for_converting_to_list))
# print(str_2)

# # my_dict = dict(str_2[i:i+1] for i in range(len(str_2)))

# # print(my_dict)
# n = [1,6,7]
# ls = ['a'], ['h']
# # d = dict(ls(key: value))
# #lsst = "".join(ls)                     
# #print(lsst)

# # s = 'dfg'
# d = dict.fromkeys(range(2))
# print(d)

# # f = {}
# l = ls[:]
# for i in d:
#     d[i] = l
# print(d)


# x=(1,'a',2,'b',3,'c')
# pp = dict(zip(x[::2],x[1::2]))
# {1: 'a', 2: 'b', 3: 'c'}

# print(pp)
#___________