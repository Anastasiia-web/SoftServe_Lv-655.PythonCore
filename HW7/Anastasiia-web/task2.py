# Task1.
# Write a Python program to check the validity of a password (input from users).

# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

import re

password = input('Enter password: ')
maxlength = len(password)
minlength = len(password)

must_have = [re.findall("\d{1}", password), re.findall("[A-Z]{1}", password), 
             re.findall("[a-z]{1}", password), re.findall("[$#@]{1}", password)]

def password_validation(password):
    if not minlength >=6 or not maxlength <=16 or not all(must_have):
        return f"Incorrect password"
    else:
        return f"Hi)"

print(password_validation(password))


# My notes

# s1 = re.match(r'I',"I want, all ^ that")
# s2 = re.match(r':',"I want, all ^ that")
# print(s1.group())
# print(s2)

# s1 = re.findall(r'a',"I want, all ^ that")
# s2 = re.match(r':',"I want, all ^ that")
# print(s1)
# print(s2)

# pattetn = re.compile("ITI")
# s1 = "I want, all ^ that IT"
# print(pattetn.findall(s1))

# q = "g jdkhjkjlk lhhgff dhjhkl"
# d = re.split(r' ', q, maxsplit=3)               # splits according to spaces or symbol : what, where, how much times
# print(d)

# q = "g jdkhjkjlk lhhgff dhjhkl"
# w = re.sub(r' ', 'G', q, 1)                     # substitudes according to : what, replace with, what, how much times
# print(w)

# x = "ghjhkj 67 ghjh6"

# print(re.findall('\d', x))

# print(re.findall('h', q))                      # finds all

# print(re.findall('h*', q))                     # * shows a place 

# print(re.findall('h+', q))                     # shows how exactly were situated

# print(re.findall('hj{1}', q))                  # shows how many times h is followed 1 time by j 

# print(re.findall('h|g', q))                    # shows how exactly were situated
