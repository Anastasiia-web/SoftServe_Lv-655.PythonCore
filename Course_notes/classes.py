#My drafts

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

#____________________
try: 
    a = int(input("Enter your number: ")) 
    if a < 4: 
        b = a/(a-3)         # throws ZeroDivisionError for a = 3 
    
    if a >= 4:      
        print("Value of b = ", b)    # throws NameError 

# note that braces () are necessary here for multiple exceptions 
except ValueError:
    print("Value Error!")
except NameError: 
    print("NameError!")
except ZeroDivisionError:
    print("ZeroDivisionError!")
except:
    print("Error!")
