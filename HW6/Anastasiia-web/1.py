# Task1. Write a function that returns the largest number of two numbers 
# (use DocStrings documentation strings in the function). 

a = 2
b = 3

def the_largest_number():

    """function that returns the largest 
       number of two numbers"""

    if a == b:
        return f"{a} is equal to {b}"
    elif a > b:
        return a
    else:
        return b

print(the_largest_number())
print(the_largest_number.__doc__)

# The same idea but using input

# a = int(input('Number 1? '))
# b = int(input('Number 2? '))

# def the_biggest_number():
#     """This function defines the biggest number"""
#     if a - b > 0:
#         print('The biggest is: ',a)
#     elif a - b == 0:
#         print('They are equal: ',a , 'and ', b)
#     else:
#         print('The biggest is: ',b)

# the_biggest_number()

# print(the_biggest_number.__doc__)






# My drafts
# name = 'Ann'
# def greet():
# 	"""This function greets the person"""
# print("Hello, "+ name +". Good morning!")

# greet()

# print(greet.__doc__)

# names= 'Ann', 'Drew', 'Ben'
# def greet(*name):
#     for name in names:
#         print('hi', name)
# greet()


# total = 0  # This is global variable.

# def my_sum(arg1, arg2):
#     total = arg1 + arg2  # Here total is local variable.
#     print("Inside the function local total : ", total)
#     return total
    

# my_sum(10, 20)
# print("Outside the function global total : ", total)
