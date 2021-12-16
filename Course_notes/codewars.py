# Task 1 
# Your collegue wrote an simple loop to list his favourite animals. 
# But there seems to be a minor mistake in the grammar, which prevents the program to work. Fix it! :)
# If you pass the list of your favourite animals to the function, you should get the list of the animals 
# with orderings and newlines added.
# For example, passing in:
# animals = [ 'dog', 'cat', 'elephant' ]
# will result in:
# list_animals(animals) == '1. dog\n2. cat\n3. elephant\n'

# Loop with mistake
# def list_animals(animals):
#     list = ''
#     for i in range(animals):
#         list += str(i + 1) + '. ' + animals[i] + '\n'
#     return list

# Solution

def list_animals(animals):
    list = ''
    for i in range(len(animals)):                        # adding "len"
        list += str(i + 1) + '. ' + animals[i] + '\n'
    return list

# Best practice

# Option 1

def list_animals(animals):
    return ''.join('{0}. {1}\n'.format(i + 1, x) for i, x in enumerate(animals))

# Option 2

def list_animals(animals):
  return ''.join(f'{i}. {animal}\n' for i, animal in enumerate(animals, 1))

# Option 3

def list_animals(animals):
    list = ''
    i=0
    for elements in animals:
        list += str(i + 1) + '. ' + elements + '\n'
        i+=1
    return list

# Option 4

def list_animals(animals):
    string = ''
    for i, animal in enumerate(animals, start=1):
        string += f'{i}. {animal}\n'
    return string

# Option 5

def list_animals(animals):
    return ''.join(str(i + 1) + '. ' + animals[i] + '\n' for i in range(0, len(animals)))

# Option 6

def list_animals(animals):
    u = ""
    i=0
    while i < len(animals):
        s=str(i + 1)
        s=s+'. '+ animals[i]
        s=s+ '\n'
        u = u + s
        i=i+1
    return u

#Task 2

# Write a program that finds the summation of every number from 1 to num. 
# The number will always be a positive integer greater than 0.
# For example:
# summation(2) -> 3
# 1 + 2
# summation(8) -> 36
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8

def summation(num):

    return sum(range(1, num + 1))
             
summation(100)

# Option 2

# def summation(num):
#     total = 0
#     for i in range(0, num+1):
#         total = total + i
#     return total

# print(summation(100))

# Option 3

# def summation(num):
#     fac = 0 
#     i = 0 
#     while i < num:
#         i += 1
#         fac = fac + i
#     return fac

# print(summation(100))


# Notes

# print(sum(range(1, 51)))

# Task 1
# Given an array of integers.
# Return an array, where the first element is the count of positives numbers and the second element 
# is sum of negative numbers.
# If the input array is empty or null, return an empty array.

# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

# TAKE OFF COMMENT - WORKING !!!
# def count_positives_sum_negatives(arr):
#     if len(arr) == 0 or arr == None:
#         return []
#     else:
#         count_positive_numbers = len([pos_number for pos_number in arr if pos_number > 0])
#         sum_negative_numbers = sum(neg_number for neg_number in arr if neg_number < 0)

#         a = [count_positive_numbers, sum_negative_numbers]

#         return a

# print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))

# count_positives_sum_negatives(arr)

# Additional task 1
# Check if a number is float
# num = 5.123
# a = type(num)

# print(f"'Float 'True") if a == float else print(f"'Not float' False")

# Additional task 2
# make all numbers in list positive

# a = [1, -5, 2, -10]
# b = [abs(x) for x in a]         # or      for x in a: abs(x)      
# print(a)

# Second option using map()
# a = [1, -5, 2, -10]
# b = map(abs, a)
# print(list(b))

# Additional task 3
# Create new arrays with negative and positive munbers from 1 array

# Option 1:
# dividing positive and negative numbers in array
# for ar in arr:
#     if ar > 0:
#         print(ar)     
#     elif ar < 0:
#         print(ar)  

# Option 2:
# positive_numbers, negative_numbers = [i for i in arr if i >= 0], [j for j in arr if j < 0]  

# print(positive_numbers)
# print(negative_numbers)

# Additional task
# Divide array into 2 arrays

# desserts = ["apple", "banana", "candy"]
# new_apple_list, new_desserts_left = [i for i in desserts if i == "apple"], [i for i in desserts if i != "apple"]
# print(new_apple_list)
# print(new_desserts_left)

# https://www.geeksforgeeks.org/python-program-to-count-positive-and-negative-numbers-in-a-list/

# Using lambda
# l = [10, 66, -93, 1]
# pos_count = 0

# pos_count = len(list(filter(lambda x: (x >= 0), l)))
  
# print("Positive numbers in the list: ", pos_count)

# Using for 

# l = [3, 5] 
# pos_count2 = 0
# l.append(2)
# print(l)

# for num in l:    
#     if num >= 0:
#         pos_count2 += 1
    
# print("Positive numbers in the list1: ", pos_count2)
