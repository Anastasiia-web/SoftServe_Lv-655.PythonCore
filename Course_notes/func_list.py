winning_lottery_numbers = [0, 4, 3, 2, 3, 1]
fake_numbers = [0, 4, 3, 2, 3, 1]


def y(): 
    print('Y') if list(fake_numbers) == list(winning_lottery_numbers) else print('N') # ternary operator !!! ELSE needs
y()                                                                                   # что делать if ... else ...


fake = list(map(lambda l: l*2, winning_lottery_numbers))  # одно и тоже lambda + map()   list(map(lambda y: y*2, my_list))
print(fake)

fak = [q*2 for q in winning_lottery_numbers]             # одно и тоже синтаксический сахар [i*2 for i in arr if ...]
print(fak)

new_list2 = list(filter(lambda x: (x%2 == 0), listl))     # отбираем чётные lambda !!! 
                                                          # Фильтру нужно 2 аргумента( как , что фильтруем)
print(new_list2)


###
###### how from input get even numbers
# inp= str(234)               # 234
# n = list(inp)               # ['2', '3', '4']
# di = [int(i) for i in n]    # [2, 3, 4]     # синтаксич сахар
# n_e = list(filter(lambda i: i%2 == 0, di))   # answer : [2, 4]            # фильтруем чётные в списке
# v = list(enumerate(di))   #  [(0, 2), (1, 3), (2, 4)]   # списке enumarate
# ind = []
# for key, value in v:
#     if value%2 ==0:
#         ind.append(key)
# print(ind)                #  [0, 2]         # считаем индексы для чётных в списке enumarate
# res_e = dict(zip(ind, n_e)) #   {0: 2, 2: 4}  сoединяем два списка в диктионари

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
    count_c += sentence.count('capitan')
print(count_c)


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

## Пример как достать 1 символ в 2 слове в списке через   names[2][0]    !!!
##                                                               
names1 = ['Amir', 'Barry', 'Charles', 'Dao']
names2 = [name.lower() for name in names1]

print(names2[2][0])             # answer : c

##  https://tproger.ru/explain/python-dictionaries/   работа со словарями !!!

class Person:                  # My practice
    def __init__(self,id):
        self.id = id

    def __str__(self):
        print(self.id)
    
obama = Person(100)
obama.__dict__['age'] = 49
Person.__str__(obama)   # 100
print(obama.age)    # 49
print(obama.__dict__)    # {'id': 100, 'age': 49}
print(Person.__dict__)   # просто список всего что на нём завязано, а не экземпляры
print(obama.age + len(obama.__dict__))                             # answer : 51