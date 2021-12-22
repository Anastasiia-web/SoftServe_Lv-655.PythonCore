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
del foo[1]                      # answer : 2  (два ключа/валью в списке осталось)
foo[1] = '10'
del foo[2]
print(len(foo))                  # answer : 2  (два ключа/валью в списке осталось)
# ##                                                                              TEST 8. What gets printed?
names = ['Amir', 'Barry', 'Charles', 'Dao']
print(names[-1][-1])             # answer:  o (the last letter of the last word)
##                                                                                TEST 9. What gets printed?
kvps = {'1': 1, '2': 2}                                 # answer : 6 
theCopy = dict(kvps)
kvps['1'] = 5       # theCopy of dictionary is NOT changed!  
sum = kvps['1'] + theCopy['1']
print(sum)                                              # answer : 6 
################################
# ##                                                               TEST 10. how to make PYTHON SCRIPT executable on Unix
answer :  the first line in the script: #!/usr/bin/env python3     
# ##                                                               TEST 11. How does BREAK CONTINUE and PASS work?
# BREAK = exit the loop
# CONTINUE = the current iteration that is running will be stopped, 
# and it will proceed with the next iteration.

# PASS is a null statement, is used as a placeholder inside loops, 
# functions, class to be implemented later
# ##                                                                                      TEST 12. What gets printed?
print(0xA + 0xa) # answer : 20 (0xA и 0xa шестнадцатеричныe представления числа 10+10=20)
# ##                                                                                      TEST 13. What gets printed?
class Person:                                         # answer : 51
    def __init__(self,id):
        self.id = id   
obama = Person(100)
obama.__dict__['age'] = 49
print(obama.age + len(obama.__dict__))                # answer : 51
# ##                                                                                      TEST 14. What gets printed?
names1 = ['Amir', 'Barry', 'Charles', 'Dao']          # answer : 12 
names2 = names1
names3 = names1[:]
names2[0] = 'Alice'
names3[1] = 'Bob'
sum = 0
for ls in (names1, names2, names3):
    if ls[0] == 'Alice':
        sum += 1
    if ls[1] == 'Bob':
        sum += 10
print(sum)              # answer : 12 (copy of list changed !!!, dict not)
# ##                                                   TEST 15. Given name = "Academy", what will name.strip("a") return?
name = "Academy"                     # answer : Academy
def s():
    return name.strip("a")           # answer : Academy
print(s())                          
# ##                                                                                      TEST 17. What gets printed?
confusion = {}                        # answer : 4
confusion[1] = 1
confusion['1'] = 2 
confusion[1] += 1  
sum = 0
for k in confusion:
    sum += confusion[k]
print(sum)                            # answer : 4
# ##                                                                                      TEST 18. What gets printed?
def f():
    pass                              # answer : <class 'NoneType'>
print(type(f()))                     
# ##                                                                                      TEST 19. What gets printed?
counter = 1                           # answer : 4
def doLotOfStuff():
    global counter
    for i in (1,2,3):
        counter += 1
doLotOfStuff()
print(counter)                         # answer : 4
# ##                                                        TEST 20. Given name = "SoftServe", what name.title() return?
name = "SoftServe"                  # answer :   Softserve
def g():
    return name.title()
print(g())
# ##                                                        TEST 21. Given variable = 5, what if variable += 2?
variable = 5                          
variable += 2                            # answer : 7
print(variable)                          
# ##                                                                                      TEST 22. What gets printed?
nums = set ([1,1,2,3,3,3,4])
print(len(nums))                         # answer : 4
# ##                                                                          TEST 23. Output of print(0.1 + 0.2 == 0.3)?
print(0.1 + 0.2 == 0.3)                  # answer : False
# ##                                                                                      TEST 24. What gets printed?
class Account:                           # answer : 123
    def __init__(self, id):
        self.id = id
        id = 666
acc = Account(123)
print(acc.id)                             # answer : 123
# ##                                                                TEST 25. What gets printed by the code snippet below?
import math
print(math.floor(5.5))                    # answer : 5
# ##                                                                                      TEST 26. What gets printed?
print(type(1/2))                          # answer :  <class 'float'>
# ##                                                                                      TEST 27. What gets printed?
d = lambda p: p *2                        # answer : 24
t = lambda p: p *3
x = 2
x = d(x)   # 4
x = t(x)   # 12
x = d(x)   # 24                         
print(x)                                  # answer : 24
# ##                                            TEST 28. value name="SoftServe IT Academy" after name.replace("o", "Q")?
name="SoftServe IT Academy"
def d():
    return name.replace("o", "Q")      # answer : SQftServe IT Academy
print(d())
# ##                                                                                      TEST 29. What gets printed?
my_tuple = ..... my_tuple.append ..... # answer : Error (an exception is thrown)
# # ##                                                                                      TEST 30. What gets printed?
print("\x48\x49!")                       # answer :  HI!
# # ##                                                                                      TEST 31. What gets printed?
boxes = {}     # print(len(crates[boxes]))          # answer : TypeError
jars = {}
crates = {}
boxes['cereal'] = 1
boxes['candy'] = 2  # {'cereal': 1, 'candy': 2}
print(boxes)  
jars['honey'] = 4   # {'honey': 4}
print(jars)
crates['boxes'] = boxes # {'cereal': 1, 'candy': 2}
crates['jars'] = jars
print(len(crates[boxes]))      # answer : TypeError: unhashable type: 'dict'

