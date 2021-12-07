# Given two ordered pairs calculate the distance between them.
# Round to two decimal places. This should be easy to do in 0(1) timing.

def distance(x1, y1, x2, y2):
    result = round(((((x2-x1)**2)+((y2-y1)**2))**0.5), 2)
    return result

distance(1, 1, 0, 0)

# Option with printing the result

def distance(x1, y1, x2, y2):
    result = round(((((x2-x1)**2)+((y2-y1)**2))**0.5), 2)
    print("distance between",(x1,y2),"and",(x1,y2),"is: ", result)

distance(1, 1, 0, 0)

# Write a function taking in a string like WOW this is REALLY amazing and returning Wow this is really amazing.
# String should be capitalized and properly spaced. Using re and string is not allowed.

def filter_words(st):
    return ' '.join(st.capitalize().split())

print(filter_words('fghkj k;lk           jhkj'))

# Option 2
def filter_words(st):
    single_spaces = " ".join(st.split())
    return single_spaces.capitalize()
filter_words("hello    world")

print(filter_words("hello                world"))

# Option with user input

def filter_words():
    string_to_capitalise = input('Enter string please: ')
    print(string_to_capitalise.capitalize())
filter_words()

#Option without cutting spaces

def filter_words(st):
    return st.capitalize()
filter_words('HELLO world!')

# We need a function that can transform a number into a string.
# What ways of achieving this do you know?

def number_to_string(num):
    return str(num)

number_to_string(67)