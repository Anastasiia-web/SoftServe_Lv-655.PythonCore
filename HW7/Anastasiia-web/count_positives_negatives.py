# Task 1
# Given an array of integers.
# Return an array, where the first element is the count of positives numbers and the second element 
# is sum of negative numbers.
# If the input array is empty or null, return an empty array.

# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

def count_positives_sum_negatives(arr):
    if len(arr) == 0 or arr == None:
        return []
    else:
        count_positive_numbers = len([pos_number for pos_number in arr if pos_number > 0])
        sum_negative_numbers = sum(neg_number for neg_number in arr if neg_number < 0)

        a = [count_positive_numbers, sum_negative_numbers]

        return a

print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))

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
# dividing pisitive and negative numbers in array
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
  
# pos_count2 = 0

# for num in l:    
#     if num >= 0:
#         pos_count2 += 1
    
# print("Positive numbers in the list1: ", pos_count2)
