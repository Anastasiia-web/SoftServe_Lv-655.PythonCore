#     lambda
#  Lambda expressions are convenient for defining not very complex functions, 
#  Usually for scenarios when you need to pass a function as a parameter into another function.

#  For example when we are using map(), filter() and reduce() …

# not used much and for really simple functions

#    [fnName] = lambda [args]: expression

# NO "return"     !!!
# if "if" needs "else"    !!!
# NO 'print' 'import' words JUST for functions with RETURN but DO NOT WRITE 'RETURN' IN LAMBDA !!!

def f(x, y): 
    if y == None: 
        y = 1 
    return x*y

# teh same as

lambda x, y: x * y if y is not None else 1

_______________________________
# my practice

def fu(x, y): 
    if y == None: 
        y = 1 
    print(x*y)

fu(3,4)


def f(x, y): 
    if y == None: 
        y = 1 
    return x*y

print(s(7,2))

b = lambda r: r * 2
print(b(3))

c = lambda w: w /3 if w>4 else print('n')

print(c(5))

x = lambda t: t *2
print(x(4))

g = lambda h, j: h * j
print(g(5, 4))


def f(x, y): 
    if y == None: 
        y = 1 
    return x*y

nn = lambda x, y: x*(y if y is not None else 1)

vv = lambda x, y: x * y if y is not None else 1

print(nn(3,2))
print(vv(3,2))


f = lambda k: k /2 if k is 7 else k 
print(f(5))
_______________

listl = [5, 6, 7, 5, 6, 7]
new_list = list(map(lambda x: x * 2, listl))           
print(listl)
print(new_list)

# m = 'hj'
# print(list(map('0',m)))

new_list2 = list(filter(lambda x: (x%2 == 0), listl))     # отбираем чётные lambda !!! 
                                                          # Фильтру нужно 2 аргумента( как , что фильтруем)
print(new_list2)

#____________ map() что делать с каждым элементом в списке!!
m = [4,3]
new_m = list(map(lambda o: o*8, m))
print(new_m)

new_even = list(filter(lambda c: c%2 == 0, m))
print(new_even)

winning_lottery_numbers = [0, 4, 3, 2, 3, 1]
fake_numbers = [0, 4, 3, 2, 3, 1]

# fake = list(map(lambda l: l*2,winning_lottery_numbers))  # одно и тоже lambda + map()   list(map(lambda y: y*2, my_list))
# print(fake)

# fak = [q*2 for q in winning_lottery_numbers]             # одно и тоже синтаксический сахар [i*2 for i in arr if ...]
# print(fak)

e = list(map(winning_lottery_numbers))
u = list(map(fake_numbers))

# ОДНО И ТОЖЕ !!!

if list(fake_numbers) == list(winning_lottery_numbers):
    print('y')
else:
    print('n')

def y(): 
    print('Y') if list(fake_numbers) == list(winning_lottery_numbers) else print('N') # ternary operator !!! ELSE needs
y()                                                                                   # что делать if ... else ...

#__________ in range(len(my_list))

li = ['Gim', 'Tim']
pi = ['G', 'T']

for i in range(len(li)):
    li[i] = pi[i]
print(li)                       # выход из цикла для печати 1 результата!!!

color = ['red', 'green', 'black', 'red', 'blue', 'yellow']   # filter()    через lambda i: i == '...', my list
red = list(filter(lambda i: i == 'red',color))               # вывод элементов из списка 
print(red)

sentences = ['capitan America', 'capitan Jak', 'capitan']      # посчитать кол-во раз в списке) цикл for + count()
count_c = 0
for sentence in sentences:
    count_c += sentence.count('capitan')
print(count_c)


count_red = 0
for word in color:
    count_red += word.count('red')
print(count_red)

count_black = 0
for i in color:
    count_black += i.count("black")
print(count_black)

winning_lottery_numbers = [0, 4, 3, 2, 3, 1]                    # max число
for i in winning_lottery_numbers:
    i = max(winning_lottery_numbers)
print(i)

color = ['red', 'green', 'black', 'red', 'blue', 'yellow']    # самле длинное слово в списке
for i in range(len(color)):
    i = max(color)
print(i)

from functools import reduce                                      # reduce !!! needs import

b = reduce(lambda a, b: a if a>b else b, winning_lottery_numbers)
print(b)
