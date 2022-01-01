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
