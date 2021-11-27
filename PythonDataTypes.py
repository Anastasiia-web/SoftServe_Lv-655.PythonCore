# immutable object types
bool = True    # true / false; true = 1, false = 0
int =12        # integer (arbitrary magnitude)
float = 12.5   # floating point number
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )  # immutable sequence of objects;  ordered sequence of items; Tuples once created cannot be modified. This type is used to write-protect data!!!
str = "My name is …"       # character string
frozenset = frozenset('qwerty')   # immutable form of set class

# mutable object types can be changed
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]   # mutable sequence of objects; ordered sequence of items
set = set('eqy') => set(['e', 'q', 'y'])   # unordered set of distinct objects; Set is an unordered collection of unique items. Just UNIQUE objects!!! (['e', 'q', 'y']) 
dict = {'name': 'john','id':6734, 'role': 'admin'}  # associative mapping (aka dictionary) ; unordered collection of key-value pairs ; Key must be immutable type and value can be of any type.

an = ['b', 's', 'd']
type(an)  # output <class 'list'>

an = ('b', 's', 'd')
type(an)  # output <class <class 'tuple'>

an = {'b', 's', 'd'}
type(an)  # output <class <class 'set'>

an = ({'b', 's', 'd'})
type(an)  # output <class 'set'>

an = 'b, s, d'
type(an)  # output <class <class 'str'>

an = {1:'b', 2:'s', 'name':'d'}
type(an)  # output <class <class 'dict'> ;    1,2,name - keys


numbers = (1, 2, 3)   # tuple   IMMUTABLE
fruits = ['apple', 1, 'banana', 'cat']   # list                        MUTABLE
alphabet = {'a': 'avoid', 'b': 'better', 'c': 'corner'}   # dict    MUTABLE
vowels = {'a', 'e', 'u'}   # set                                    MUTABLE

print(numbers)   #output (1, 2, 3)
print(fruits)    #output ['apple', 1, 'banana', 'cat']          
print(alphabet)  #output {'a': 'avoid', 'b': 'better', 'c': 'corner'}
print(vowels)    #output {'e', 'a', 'u'}

print(numbers)   #output (1, 2, 3)
print(fruits)    #output ['apple', 'banana', 'cat']          
print(alphabet)  #output {'a': 'avoid', 'b': 'better', 'c': 'corner'}
print(vowels)    #output {'e', 'a', 'u'}

fruits = ['apple', 1, 'banana', 'cat']   # list
fruits[1] = 2  
fruits     # output  ['apple', 2, 'banana', 'cat'] DUE TO indexing place from 0 -> [0, 1, 2, 3] 


# Immutable vs Mutable
x = 'foo'
y = x
print (x)           # foo
y + = 'bar'
print (x)           # foo

x = 'something'        # immutable type
y = x
print (x)              # some statement that operates on y
print (x)              # prints the SAME thing


x = [1, 2, 3]
y = x
print (x)             # [1, 2, 3]
y += [3, 2, 1]
print (x)             # [1, 2, 3, 3, 2, 1]

x = [something]        # mutable type : list [], set(), dict {1: 'a'}
y = x
print (x)              # some statement that operates on y
print (x)              # might print something DIFFERENT

#To quickly test if a type is mutable or not, is to use id() built-in function

i = 1
id(i)
#output ***704
i += 1
i
#output 2 
id(i)
#output ***736 (different from ***704)

a = [1]
id(a)
#output ***416
a.append(2)
a
#output [1, 2]
id(a)
#output ***416 (same with the above id)

a=list(range(10))
print(a)
#output [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b=a
print(b)
#output [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(id(a),id(b))
#output **6 **6
a.append(10)
print(a)
#output [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(b)
#output [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(id(a),id(b))
#output **6 **6 THE SAME id !!!

a=1                          #a=1
b=a                          #b=1
print(id(a),id(b))
#output  *6 *6
b+=1                       #b=2
print(id(a),id(b))
#output  *6 *2  DIFFERENT id !!!
c=2                         #c=2
print(id(a),id(b),id(c))
#output  *6 *2 *2   LAST TWO THE SAME!!! the object was already created = saving memory

d=1000
k=d+1                     #k=1001
d+=1                      #d=1001
print(id(d),id(k))
#output 20898480 20898464  Different!!!

# TYPE CONVERSION  (implicit type conversion (without user), explicit type conversion)
a = int("34")                       # a = 34
a = int ("0100",2)                  # a = 4
a = int(6.7)                        # a = 6
b = int("0xfe76214",16)             #long  b=266822164L 
b = int("70",8)                     #b=56
b = float("3")                      # b = 3.0
c = eval("3, 5, 6")                 # c = (3,5,6)
c = eval("3 + 5 + 6")               # c = 14

list('Hello')   #output ['H', 'e', 'l', 'l', 'o']
set([1,2,3])    #output {1, 2, 3}
set(['h','e','l'])  # {'e', 'l', 'h'}
tuple([1,2,3])      # (1, 2, 3)
dict([[1, 'a'], [2, 'b'], [3, 'c']]) # {1: 'a', 2: 'b', 3: 'c'}

# Explicit type conversion

a = 31
b = int("41")
print(a+b)    #outcome 72

print(r"Hello \n world!!!")      # print("Hello \n world!!!")

# This prints out "Hello, John!“
name = 'John'
print("Hello, %s!" % name)

# This prints out "John is 23 years old.“
name = 'John'
age = 23
print("%s is %d years old." % (name, age))

# This prints out "John is 23 years old. Your sallary is 999.990 $"
name = 'John'
age = 23
salary = 999.99
print("%s is %d years old. Your sallary is %.3f $" % (name, age, salary))

# NEW format() method

# default(implicit) order
default_order = "{}, {} and {}".format('John','Bill','Sean')

# order using positional argument
positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')

# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')

# formatting integers
"Binary representation of {0} is {0:b}".format(12)
'Binary representation of 12 is 1100'

# formatting floats
"Exponent representation: {0:e}".format(1566.345)
'Exponent representation: 1.566345e+03'

# round off
"One third is: {0:.3f}".format(1/3)
'One third is: 0.333'

# Common Python String Methods

str = 'programiz'
print('str = ', str)

#first character
print('str[0] = ', str[0])

#last character
print('str[-1] = ', str[-1])

#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])

#slicing 6th to 2nd last character
print('str[5:-2] = ', str[5:-2])

"PrOgRaMiZ".lower()   # 'programiz‘

"PrOgRaMiZ".upper()   # 'PROGRAMIZ‘

"This will split all words into a list".split()   #  ['This', 'will', 'split', 'all', 'words', 'into', 'a', 'list']

'  '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string'])  # 'This will join all words into a string‘

'Happy New Year'.find('ew')   # 7

'Happy New Year'.replace('Happy','Brilliant')   #  'Brilliant New Year'