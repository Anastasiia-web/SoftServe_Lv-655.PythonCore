## лучший List Practice!!! https://devpractice.ru/python-lesson-7-work-with-list/ 
## функции с примерами + оттуда ссылка на “Уроке 15. Итераторы и генераторы“ 
#№ https://devpractice.ru/python-lesson-15-iterators-and-generators/

## Nested lists !!! 10 Important Tips for Using Nested Lists in Python
## https://betterprogramming.pub/10-important-tips-for-using-nested-lists-in-python-38ceca68be35
## 

## https://pythonru.com/primery/python-spiski-primery

## https://pythonworld.ru/tipy-dannyx-v-python/spiski-list-funkcii-i-metody-spiskov.html


# n = int(input("?: "))                               # факториал
# fact = 1
# while n > 0:
#     fact = fact * n
#     n = n-1
# print(fact)
########                                              # фибоначи
# a, b = 0, 1
# while b <= 5:
#     print(b)
#     a, b = b, a + b

#######
v = ['h', 'd']
s = list(filter(lambda x: x == 'd', v))                # отфильтровать слово в списке  filter
print(s)
#######
f = v.index("d")                                       # найти индекс слоа с списке
print(v)
print(f)
#######

# Option 1                                             # удаляем слово из списка даже повторяющееся

arr = ['test', 'pest', 'vest', 'pest']

for i in arr:
    arr.remove('pest')
print(arr)

# Option 2

arr = ['test', 'pest', 'vest', 'pest']

for i in arr:                                          # удаляем слово из списка даже повторяющееся
    if 'pest' in arr:
        del arr[arr.index('pest')]

print(arr)
######

w = [0, 4, 3, 2, 3, 1]

a = list(map(lambda x: x*2, w))                         # умножили на 2 всё в списке
print(a)

fa = [q*2 for q in w]                                   # одно и тоже синтаксический сахар [i*2 for i in arr if ...]
print(fa)

r = []                                                  # новый список из чётных умноженных на 2 из старого списка
for i in w:
    if i%2 == 0:
        r.append(i * 2)
print(r)

# from functools import reduce                                      # reduce !!! needs import

# p = [0, 4, 3, 2, -3, 3, 1]

# from functools import reduce                                      # reduce !!! needs import
# winning_lottery_numbers = [0, 4, 3, 2, 3, 1]
# b = reduce(lambda a, b: a if a>b else b, winning_lottery_numbers)
# print(b)
# print(winning_lottery_numbers)

sentences = ['capitan America', 'capitan Jak', 'capitan']      # посчитать кол-во раз в списке) цикл for + count()
count_c = 0
for sentence in sentences:
    count_c += sentence.count('capitan')
print(count_c)

winning_lottery_numbers = [0, 4, 13, 2, 3, 1]                   # найти максимальное число в списке
for i in winning_lottery_numbers:
    s = max(winning_lottery_numbers)
print(s)

words = ['learn', 'daaaaaaaaaaaaa', 'python']                   # самле длинное слово в списке
print(max(words, key=len))




h = ['lkj', 'hjk']                                                          # как в списке найти и посчитать символ
k = list(''.join(h))
y = list(filter(lambda i: i == 'j', k))
d = y.count('j')

print(list(k))
print(list(y))
print(d)

#######

h = ['lkj', 'hjk']                                                          # как в списке найти и посчитать символ
k = list(''.join(h))
y = list(filter(lambda i: i == 'j', k))
d = y.count('j')

print(list(k))
print(list(y))
print(d)

###############

my_list = [1, 's', 2, 3, 4, 5]                                          # вставляем в список на индекс
my_list.insert(1, 2)
print(my_list)

## СПИСКИ СПИСКОВ НА ОСНОВЕ
## https://betterprogramming.pub/10-important-tips-for-using-nested-lists-in-python-38ceca68be35

## 3. How to flatten a nested list?

words = ['learn', ['ge', 'ki'], 'daaaaaaaaaaaaa', 'python']          # как в списке списка найти и посчитать символ
#???
words_general = [element for sub_list in words for element in sub_list]
print(words_general)

for i in words_general:
    s = words_general.count('a')
print(s)

my_list=[[1,2],[4,5,6],[7,8]]
result=[v1 for sub_list in my_list for v1 in sub_list]
print(result)  #Output:[1, 2, 4, 5, 6, 7, 8]

##############
## ЛУЧШЕ ещё разбить на символы отдельно и уже потом искать и считать символ !!!

wo = ['learn', ['ge', 'ki'], 'daaaaaaaaaaaaa', 'python']          # как в списке списка найти и посчитать символ

wo_g = [i for subclass in wo for i in subclass]

wo_g_s = ("".join(wo_g))
print(wo_g_s)
l_wo_g_s = list(wo_g_s)
print(l_wo_g_s)

for i in l_wo_g_s:
    symbols_number = l_wo_g_s.count('e')
print(symbols_number)
############
