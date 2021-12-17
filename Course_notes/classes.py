#My drafts

# Shift + Tab  - сдвиг влево блока кода
# Tab  - сдвиг вправо блока кода

# def list_animals(animals):   # SUBMITED))) but not adopted for new animals in the list !!!
#     list = []
#     for i in animals:
#         list = str("1. " + i + "\n2. " + animals[1] + "\n3. " + animals[2] + "\n")
#         return list

# print(list_animals([ 'dog', 'cat', 'elephant' ]))

# def list_animals(animals):                   
#     list = ''
#     for i in range(len(animals)):                     # SOLUTION add "len"
#         list += str(i + 1) + '. ' + animals[i] + '\n'
#     return list

# print(6/4.5)               # True division   #  1.3333333333333333
# print(6 //4.5)             # Rouded result (without reminder) #  1.0



# class Parent(object):
   
#     def isParOrPChild(self):
#         return True
#     def who(self):
#         return 'parent'

# class Child (Parent):
#     def who (self):
#         return 'child'

# x = Parent()
# print(x.who(), x.isParOrPChild())

# x = Child()
# print(x.who(), x.isParOrPChild())

# # parent True
# # child True

# class Parent(object):
#     def foo(self):
#         return 'who'
#     def foo(self, s):
#         return 'who ' + s
# x = Parent()

# print(x.foo('me'))

# class Parent(object):
#     def foo(self, *arg):
#         if arg:
#             suma = 0
#             str_join = ""
#             for i in arg:
#                 if isinstance(i, int):
#                     suma += i
#                 elif type(i) == str:
#                     str_join += i
#             return 'sum: {0}  str_join: {1}'.format(suma, str_join)
#         else:
#             return 'foo'

# x = Parent()
# print(x.foo("boo"))
# print(x.foo("boo", 100, 300, [1,2,3], "koo", 2.5))
# print(x.foo())

# In general case to get the parent class the function super is applied:
# class Child(Parent):
#     def __init__ (self):
#     super(Child, self).__init__(self)
#____________________
# class Lesson:
#     def __init__ (self, x, y):
#         self.x = (x)
#         self.x = (y)
#     def beginning():
#         pass

# p = Lesson(0, 0)
# print(p)

# #____________________
# try: 
#     a = int(input("Enter your number: ")) 
#     if a < 4: 
#         b = a/(a-3)         # throws ZeroDivisionError for a = 3 
    
#     if a >= 4:      
#         print("Value of b = ", b)    # throws NameError 

# # note that braces () are necessary here for multiple exceptions 
# except ValueError:
#     print("Value Error!")
# except NameError: 
#     print("NameError!")
# except ZeroDivisionError:
#     print("ZeroDivisionError!")
# except:
#     print("Error!")


X = set('spam') # В 2.6 и 3.0 можно создавать из последовательностей
Y = {'h', 'a', 'm'} # В 3.0 можно определять литералы множеств
X, Y
# ({'a', 'p', 's', 'm'}, {'a', 'h', 'm'})
print(X, Y)
X & Y # Пересечение
print(X & Y)
#{'a', 'm'}

X | Y # Объединение
# {'a', 'p', 's', 'h', 'm'}
print(X | Y)

#X – Y # Разность
# {'p', 's'}
print(''.join(X - Y))     # "".join(array_to_str) !!!


# Генерация списка чисел в рэнже от 0 до 10
#max = range(10) #Генерування послідовності чисел від 0 до 9
for num in range(10): #Пока переменная number (которая каждый раз увеличивается на единицу) входит в список…
    print(num)

list2=['яблуко ' ,'груша','ананас'] # Створення списку з даними рядкового типу
i = 0
while i <= 2:
    print(list2[i]+str(i)) # str(i) - перетворення числового типу в рядковий
    i += 1

g = """hjk
mnm,m/.,
mnkmkm
"""

print(g)

# print(list2.index("яблуко"))                 № возвращает индекс
list3 = [x for x in list2 if x.strip()!='']    # обрезает спэйсы в списке
print(list3)
list4 = [x for x in list3[0] if x.strip()!='']
b = "".join(list4)
print(b)
print(list3.extend([b]))       # не могу добавить яблоко в список!!!

#_______________

# db = MySQLdb.connect("localhost", "username", "password", "dbname")
# cursor = db.cursor()
 
# sql = """SELECT `name`, `age` 
#       FROM `ursers` 
#       ORDER BY `age` DESC"""


# cursor.execute(sql)
# results = cursor.fetchall()

# for row in results:
#     print(row[0] + row[1])
 
# db.close()
#__________
if 'грушrа' in list2:
    print("hi")

for l in list2:
    a = filter(list2, 'груша')
print(a)
print(list2)

# if filter(list2, 'грRуша'):
#     print(True)

n =[]                  # наполнение списка цифрами
o = 0
while o < 10:
    o = o+ 1
    n.append(o)
print(n)

h = list("jkjlkjlk")   # строка в список
print(h)

words = ['cat', 'window', 'defenestrate']
words_length = 0

for word in words:
    words_length += len(word)

# "cat" length is 3
# "window" length is 6
# "defenestrate" length is 12
print(assert words_length == (3 + 6 + 12))


  

