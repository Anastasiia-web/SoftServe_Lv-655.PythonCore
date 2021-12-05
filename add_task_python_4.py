# Create a list that contains elements of integer type, then use the loop to change the type of these elements to a floating type. 
# use the built-in float () function)

i = 0
my_list =[4, 5]
float_num = [float(i) for i in my_list]
#print([float(i) for i in my_list])
print(type(my_list))
print(type(my_list[0]))
print(type(float_num))
print(type(float_num[0]))


# My drafts

# Python Data Types
# https://www.programiz.com/python-programming/variables-datatypes


# https://blog.finxter.com/how-to-convert-a-string-list-to-a-float-list-in-python/
# List comprehension is a compact way of creating lists. 
# The simple formula is [expression + context]. Expression: What to do with each list element? Context: What elements to select? 
# The context consists of an arbitrary number of for and if statements.

# list of strings to a list of floats 

# a = list('6')
# print([float(x) for x in a])
# print(type(a))
# print(type(a[0]))

# f = list('10')
# print(f)
# print(type(f))
# print(type(f[0]))

# for i in f:
#     float(f)
#     print(f)
# print(type(f))
