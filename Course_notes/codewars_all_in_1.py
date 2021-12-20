# 1. Is string upper?

inp = 'hjjk'
def is_uppercase():
    return inp.isupper()
print(is_uppercase())

# 2. Sort list

def sorter():
    textbooks= ['Uio', 'fgh', 'Po']
    textbooks = sorted(textbooks, key=lambda name:name.lower())
    return textbooks

print(sorter())

# 3 New time

def shorten_to_date(long_date):
    index = long_date.index(',')
    new_string = long_date[:index]
    return (new_string)

# 4 Color ghost

import random

class Ghost():
  colors = ["white", "yellow", "purple", "red"]
  
  def __init__(self):
    self.color = random.choice(Ghost.colors)

# 5 Classy classes

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.info=f'{self.name}s age is {self.age}'
        
    def getInfo(self):
        return self.info

# 6 super ball

class Ball(object):
  def __init__(self, type = "regular"):
    self.ball_type = type


# 7 Adam & Eve

def God():
		return (Man(), Woman())
	
	
class Human:
	pass
	
	
class Man(Human):
	pass
	
	
class Woman(Human):
	pass


# 8. # https://www.codewars.com/kata/grasshopper-summation/train/python

# Напишіть програму, яка знаходить суму всіх чисел від 1 до введеного числа. 
# Число завжди буде натуральним числом більше 0.

summation = lambda x: sum(range(1, x + 1))

# 9. Animals fix loop

def list_animals(animals):
    list = ''
    for i in range(len(animals)):
        list += str(i + 1) + '. ' + animals[i] + '\n'
        return list

# 10. # https://www.codewars.com/kata/double-char/train/python

# Потрібно повернути рядок, у якому кожен символ 
# (з урахуванням регістру) повторюється один раз.

def double_char(s):
    return ''.join(c * 2 for c in s)

# 11 
# https://www.codewars.com/kata/reverse-list-order
# In this kata you will create a function that takes in a list and 
# returns a list with the reverse order.

def reverse_list(l):
    reverse = reversed(l)
    return list(reverse)

# 12 # https://www.codewars.com/kata/count-of-positives-slash-sum-of-negatives
# Повернути масив, де перший елемент - це кількість додатніх чисел, 
# а другий - сума від’ємних чисел.

def count_positives_sum_negatives(arr):
    return [len([x for x in arr if x > 0])] + [sum(y for y in arr if y < 0)] if arr else []

# 13. # https://www.codewars.com/kata/514b92a657cdc65150000006/train/python

# Якщо ми перерахуємо всі натуральні числа нижче 10, 
# кратні 3 або 5, то отримаємо 3, 5, 6 і 9. 
# Сума цих кратних дорівнює 23.
# Має повертатися сума всіх кратних 3-м або 5-м чисел.

def solution(number):
    result = 0
    for i in range(0,number):
        if i%3 == 0 or i%5 == 0:
            result = result + i
    return result

# 14 # https://www.codewars.com/kata/is-this-my-tail/train/python

# О ні, Тіммі створив нескінченний цикл! 
# Допоможіть Тіммі знайти та виправити помилку у його незавершеному циклі for!

def create_array(n):
    res=[]
    i=1
    while i<=n: 
        res += [i]
        i+= 1
    return res
# ###################################
def create_array(n):
    return [i for i in range(1,n+1)]

# 15 # https://www.codewars.com/kata/no-yelling
# Write a function taking in a 
# string like WOW this is REALLY amazing and 
# returning Wow this is really amazing. 
# String should be capitalized and properly spaced. 
# Using re and string is not allowed.

# def filter_words(st):
#     return ' '.join(st.capitalize().split())

def filter_words(st):
    my_str= st.lower()
    str_2= my_str.capitalize()
    result= ' '.join(str_2.split())
    return result

# 16 # https://www.codewars.com/kata/simple-find-the-distance-between-two-points
# Simple: Find The Distance Between Two Points

# Дано дві впорядковані пари, обчисліть відстань між ними. 
# Округліть до двох знаків після коми. 

def distance(x1, y1, x2, y2):
    return round(((x2 - x1)**2 + (y2 - y1)**2)**0.5, 2)


# 17 #https://www.codewars.com/kata/will-you-make-it
#Will you make it
# Ви кемпінгували з друзями далеко від дому, 
# але коли настає час повертатися назад, 
# ви розумієте, що у вас закінчується паливо, 
# а найближчий насос - за 50 миль! 
# Ви знаєте, що в середньому ваша машина 
# проїжджає приблизно 25 миль на галон. 
# Залишилося 2 галони. Враховуючи ці фактори, 
# напишіть функцію, яка повідомляє, 
# чи можна дістатися до насоса чи ні. 
# Функція повинна повертати true, 
# якщо це можливо, і false, 
# якщо ні. Вхідні значення завжди додатні.

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump<=mpg*fuel_left

# 17. # https://www.codewars.com/kata/is-this-my-tail/train/python

# У зоопарк прибуло кілька нових тварин. Власник зоопарку стурбований тим, 
# що, можливо, у тварин немає правильних хвостів. Щоб допомогти, ви повинні 
# виправити непрацездатну функцію, щоб переконатися, що другий аргумент (хвіст) 
# збігається з останньою літерою першого аргументу (тіло) - інакше хвіст не вміститься!
# Якщо хвіст правильний, поверніть true, інакше поверніть false.


def correct_tail(body, tail):
	sub = body[-1]
	if sub == tail:
		return True
	else:
		return False

# 18. # https://www.codewars.com/kata/are-you-playing-banjo

# Створіть функцію, яка відповідає на запитання "Ви граєте на банджо?".
# Якщо ваше ім'я починається з літери "R" або малої літери "r", то ви граєте в банджо!
# Функція приймає ім'я як єдиний аргумент і повертає один із наступних рядків:
# name + "грає на банджо"
# name + "не грає на банджо"

def areYouPlayingBanjo(name):
    if name[0].lower()=="r":
        return name + "plays banjo"
    return name + "does not play banjo"

# 19. #https://www.codewars.com/kata/counting-sheep-dot-dot-dot/train/python
#Counting sheep

# Розглянемо масив / список овець, де деякі вівці можуть бути відсутні 
# на своєму місці. Необхідно написати функцію, яка підраховує кількість 
# овець, що присутні в масиві (справжні засоби присутні).


def count_sheeps(arrayOfSheeps):
  return arrayOfSheeps.count(True)

# 20. #https://www.codewars.com/kata/will-there-be-enough-space/train/python
#Will there be enough space
# Bob is working as a bus driver. 
# However, he has become extremely 
# popular amongst the city's residents. 
# With so many passengers wanting to get 
# aboard his bus, he sometimes has to face 
# the problem of not enough space left on the bus!
#  He wants you to write a simple program telling him 
# if he will be able to fit all the passengers.
# You have to write a function that accepts three parameters:

# написати функцію, яка приймає три параметри:

# cap - кількість людей, яких може вмістити автобус, за винятком водія.
# on - це кількість людей в автобусі, крім водія.
# wait - це кількість людей, які чекають, щоб сісти в автобус, за винятком водія.
# Якщо місця достатньо, поверніть 0, а якщо немає, поверніть кількість пасажирів, 
# яких він не може взяти.

def enough(cap, on, wait):
    if on + wait > cap:
       return on + wait - cap
    else:
        return 0

# 20 #https://www.codewars.com/kata/convert-boolean-values-to-strings-yes-or-no

# Завершіть метод, який приймає булеве значення, 
# і поверніть рядок "Так" для true, або рядок "Ні" для false.

def bool_to_word(boolean_data):
   if boolean_data:
      return "Yes"
   else :
      return "No"

# 21 #http://www.codewars.com/kata/all-star-code-challenge-number-18/python
#All Star Code Challenge #18
# Створіть функцію, яка приймає 2 аргументи(типу string)
# і повертає ціле число від кількості випадків

def str_count(strng, letter):
    return strng.count(letter)

# 22  reverse string

def reverse(st):
    return ' '.join(reversed(st.split())) 

# 23 Jenny's secret

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {}!".format(name)

# 24 Convert num to str

def number_to_string(num):
    return str(num)
