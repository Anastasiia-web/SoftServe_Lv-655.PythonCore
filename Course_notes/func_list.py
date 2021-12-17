winning_lottery_numbers = [0, 4, 3, 2, 3, 1]
fake_numbers = [0, 4, 3, 2, 3, 1]


def y(): 
    print('Y') if list(fake_numbers) == list(winning_lottery_numbers) else print('N') # ternary operator !!! ELSE needs
y()                                                                                   # что делать if ... else ...


fake = list(map(lambda l: l*2,winning_lottery_numbers))  # одно и тоже lambda + map()   list(map(lambda y: y*2, my_list))
print(fake)

fak = [q*2 for q in winning_lottery_numbers]             # одно и тоже синтаксический сахар [i*2 for i in arr if ...]
print(fak)

new_list2 = list(filter(lambda x: (x%2 == 0), listl))     # отбираем чётные lambda !!! 
                                                          # Фильтру нужно 2 аргумента( как , что фильтруем)
print(new_list2)


#    [fnName] = lambda [args]: expression                   # lambda

# NO "return"     !!!
# if "if" needs "else"    !!!
# NO 'print' 'import' words JUST for functions with RETURN but DO NOT WRITE 'RETURN' IN LAMBDA !!!

def f(x, y): 
    if y == None: 
        y = 1 
    return x*y

# teh same as

lambda x, y: x * y if y is not None else 1

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
    cap_count += sentence.count('capitan')
print(cap_count)


winning_lottery_numbers = [0, 4, 3, 2, 3, 1]                # max число
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

#______________

a=[]

def foo():
    a.append(1)
    print(a)

foo()

h = str(d)                                              # как в списке списка найти и посчитать символ
k = list(''.join(h))
y = list(filter(lambda i: i == 'j', k))
d = y.count('j')

print(list(k))
print(list(y))
print(d)