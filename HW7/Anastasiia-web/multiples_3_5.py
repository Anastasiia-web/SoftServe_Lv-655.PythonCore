# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. 
# Additionally, if the number is negative, return 0 (for languages that do have them).
# Note: If the number is a multiple of both 3 and 5, only count it once.

def solution(number):
    result = []
    for i in range(0, number):
        if i % 3 == 0 or i % 5 == 0:
            result.append(i)
    return sum(result)

print(solution(4))

# Best practice 1

def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

solution(7)

# Best practice 2

def solution(number):
    sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

solution(6)

# Notes

# Odd / even numbers
# number = 650
# print('even') if number % 2 == 0 else print('odd')

# fruits = ['apple', 'banana', 'cherry']
# fruits.append("orange")

#  Make an array out of number 123 like [1,2,3]
# Option 1
# list_numbers = [int(i) for i in str(number)]   #  or   print([int(num) for num in "123456"])  # [1, 2, 3, 4, 5, 6]

# Option 2
# number = str(12)                               #  or   print(list(map(int, "123456")))  # [1, 2, 3, 4, 5, 6]
# maped = map(int, number)
# listed = list(maped)
# print(listed)                                                   # output [1, 2]

# put into array numbers as string
# print(list(str(123456)))
