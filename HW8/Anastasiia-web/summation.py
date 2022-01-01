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