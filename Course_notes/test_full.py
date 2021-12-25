##    *                                                            TEST  2. What is the output of the following code:      
print(type(lambda:None))  # answer :  <class 'function'>    

# ##   *                                                            TEST  3. What gets printed?
def d(p, **p2):                 # answer :  <class 'dict'>
    print(type(p2))
d('capitals', Arisona = 'hj', California = 'Sacramento')

# ##                                                               TEST 4. What gets printed?
names1 = ['Amir', 'Barry', 'Charles', 'Dao']
names2 = [name.lower() for name in names1]      # answer : c 
print(names2[2][0])             # answer : c 

# ##  *                                                             TEST 5. What gets printed?

names1 = ['Amir', 'Barry', 'Charles', 'Dao']

if "amir" in names1:            # answer : 2 (с маленькой буквы)
    print(1)
else:
    print(2)

# ##                                                                TEST 6. What gets printed?
foo = {1: '1', 2: '2', 3: '3'}
del foo[1]
# print(foo)   # {2: '2', 3: '3'}
foo[1] = '10'
# print(foo)   # {2: '2', 3: '3', 1: '10'}
del foo[2]     # {3: '3', 1: '10'}
print(len(foo))                  # answer : 2  (два ключа/валью в списке осталось)

# ##                                                                           TEST 8. What gets printed?
names = ['Amir', 'Barry', 'Charles', 'Dao']
print(names[-1][-1])  # answer:  o (the last letter of the last word)

# ##                                                                           TEST 9. What gets printed?
kvps = {'1': 1, '2': 2}
theCopy = dict(kvps)     # через конструктор dict() глубокая копия => другой объект !!!
# print(kvps)       # {'1': 1, '2': 2}
# print(theCopy)    # {'1': 1, '2': 2}
kvps['1'] = 5     # theCopy of dictionary is NOT changed !!!!
# print(kvps)       # {'1': 5, '2': 2}
# print(theCopy)    # {'1': 1, '2': 2}
sum = kvps['1'] + theCopy['1']              # answer : 6 
print(sum)                                 

################################
# ##                                                               TEST 10. how to make python script executable on Unix
# answers    3 :  scripts  должны быть проранены
#            4 :  the first line in the script: #!/usr/bin/... python   
#   
# ##                                                               TEST 11. How does break continue and pass work?
# break = exit the loop.

# continue = will be stopped the current iteration that is running, 
# and it will proceed with the next iteration.

# Pass Statement is used as a placeholder inside loops, functions, 
# class, if-statement that is meant to be implemented later. Python pass is a null statement

# ##                                                                                      TEST 12. What gets printed?
print(0xA + 0xa) # answer : 20 (0xA и 0xa шестнадцатеричныe представления числа 10 => 20)
# ##                                                                                      TEST 13. What gets printed?
class Person:                 
    def __init__(self,id):
        self.id = id
    
obama = Person(100)
obama.__dict__['age'] = 49
print(obama.age + len(obama.__dict__))                             # answer : 51
print(obama.age)   # 49
print(len(obama.__dict__))  # 2   as (2 attr: age, id)

##                                                                                      TEST 14. What gets printed?
names1 = ['Amir', 'Barry', 'Charles', 'Dao']  # answer : 12
names2 = names1      # shalow copy !!!
names3 = names1[:]   # deep copy !!!
# print(id(names1))
# print(id(names3))
names2[0] = 'Alice'
names3[1] = 'Bob'

sum = 0
for ls in (names1, names2, names3):
    if ls[0] == 'Alice':
        sum += 1
    if ls[1] == 'Bob':
        sum += 10

print(sum)                          # answer : 12 (2 'Alice' + 10 'Bob')

##                                                   TEST 15. Given name = "Academy", what will name.strip("a") return?
name = "Academy"
def s():
    return name.strip("a")
print(s())                          # answer : Academy

##                                                                                      TEST 17. What gets printed?
confusion = {}
confusion[1] = 1
confusion['1'] = 2  # {1: 1, '1': 2}
confusion[1] += 1   # {1: 2, '1': 2}
# print(confusion)
sum = 0
for k in confusion:
    sum += confusion[k]
print(sum)                           # answer : 4

##                                                                                      TEST 18. What gets printed?
def f():
    pass
print(type(f()))                     # answer : <class 'NoneType'>

# ##                                                                                      TEST 19. What gets printed?

counter = 1
def doLotOfStuff():
    global counter
    for i in (1,2,3):
        counter += 1
doLotOfStuff()
print(counter)                         # answer : 4

# ##                                                        TEST 20. Given name = "SoftServe", what name.title() return?
name = "SoftServe"        # answer :   Softserve
def g():
    return name.title()
print(g())

#                                                        TEST 21. Given variable = 5, what if variable += 2?
variable = 5
variable += 2
print(variable)                          # answer : 7

##                                                                                      TEST 22. What gets printed?
nums = set ([1,1,2,3,3,3,4])          # убирает дубликаты !!! set
print(len(nums))                         # answer : 4

##                                                                          TEST 23. Output of print(0.1 + 0.2 == 0.3)?

print(0.1 + 0.2 == 0.3)               # answer : False для дробных чисел !!!

##                                                                                      TEST 24. What gets printed?

class Account:
    def __init__(self, id):
        self.id = id
        id = 666

acc = Account(123)
print(acc.id)                              # answer : 123

##                                                                TEST 25. What gets printed by the code snippet below?
import math

print(math.floor(5.5))                       # answer : 5 в наименьшую сторону !!!

##                                                                                      TEST 26. What gets printed?
print(type(1/2))                             # answer :  <class 'float'>

##                                                                                      TEST 27. What gets printed?

d = lambda p: p *2
t = lambda p: p *3
x = 2
x = d(x)   # 4
x = t(x)   # 12
x = d(x)   # 24                         
print(x)                                      # answer : 24     считается по порядку увеличивая х!!!

##                                            TEST 28. value name="SoftServe IT Academy" after name.replace("o", "Q")?
name="SoftServe IT Academy"     
name.replace("o", "Q")    # answer : SоftServe IT Academy  (НЕ вызываем!!!)
print(name)

# def d():
#     return name.replace("o", "Q")      # answer : SQftServe IT Academy   если вызываем!!!
# print(d())

##                                                                                      TEST 29. What gets printed?

my_tuple = ..... my_tuple.append ..... # answer : Error (an exception is thrown)

# ##                                                                                      TEST 30. What gets printed?
print("\x48\x49!")                       # answer :  HI!

# 2
# They are called hexadecimal escape sequences.
# If you are using firefox or chrome, they can turn it into a text if you just copypaste a string 
# like '\x48\x49' to the their console. But you could also use this http://jsfiddle.net/HHfdp/show/
# find out more about these in the Python documentation for String Literals.

# ##                                                                                      TEST 31. What gets printed?
boxes = {}     # print(len(crates[boxes]))    # answer : TypeError: unhashable type: 'dict'
jars = {}
crates = {}

boxes['cereal'] = 1
boxes['candy'] = 2  # {'cereal': 1, 'candy': 2}
print(boxes)  
jars['honey'] = 4   # {'honey': 4}
print(jars)
crates['boxes'] = boxes # {'cereal': 1, 'candy': 2}
crates['jars'] = jars

print(len(crates[boxes]))                # answer : TypeError: unhashable type: 'dict' (You're trying
                                          # to use a dict as a key to another dict or in a set . 
                                          # That does not work because the keys have to be hashable.)
##########
# ADDITIONAL TASKS

#                                         # Test task : What does the following code do?
def a(b, c, d): pass                     # answer : defines a function which passes its parameteres throuh

#                                        Test task : Which of the following data structures can be used with the "in" 
#                                        operator to check if an item is in the data structure?
answer : All the above     (dictionary, list, set)

#                                                       Test task : What gets printed?
def addItem(ListParam):
    ListParam += [1]

mylist = [1, 2, 3, 4]
addItem(mylist)
print(len(mylist))           # answer : 5

#                                                       Test task : What gets printed?
one = chr(104)
two = chr(105)
print(one + two)               # answer : hi

#                                                       Test task : What gets printed?
def dostuff(param1, *param2):     
    print(type(param2))     # answer : <class 'tuple'>
dostuff('appels', 'bananas', 'cherry', 'dates')

#                                                       Test task : What gets printed?
def myfunc(x, y, z, a):
    print(x + y)              # answer : 3
nums = [1, 2, 3, 4]
myfunc(*nums)                 # распаковываем параметры через *

#                                                       Test task : What gets printed?
x = True
y = False
z = False

if not x or y:
    print(1)
elif not x or y and z:
    print(2)
elif not x or y or not y and x:
    print(3)                       # anwser : 3 
else:
    print(4)

##                                                       Test task : What gets printed?
a = [1, 2, 3, None, (), [],]
print(len(a))                        # anwser : 6
##                                                       Test task : What gets printed?
x = True
y = False
z = False

if x or y and z:
    print("yes")                      # answer : yes
else:
    print('no')
##                                                       Test task : What gets printed?
name = "snow storm"
name[5] = 'X'
print(name)          # answer : ERROR (TypeError: 'str' object does not support item assignment)

##                                                                Test task
def p(str):
    print('+++' + str + "+++")
category = 1
text = 's'
p("{} and {}".format(category, text))  # answer : +++1 and s+++

##                                                  Test task
n = {}
n[(1,2,4)] = 8
print(n)    # {(1, 2, 4): 8}

##                                                            Test task
name = "snow storm"    
print(name[6:8])
f =(3,4)
print(type(f))   # answer : to ( ПОСЛЕДНЮЮ ЦИФРУ (индекс) НЕ УЧИТЫВАЕТ !!!)

##                                                         Test task
x = 'f'
y = 2
print(x+y)     # answer : TypeError: can only concatenate str (not "int") to str



