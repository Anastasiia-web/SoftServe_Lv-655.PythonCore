# Task1. In the range from 1 to 10 determine 
# even numbers that are divisible by 2,
# odd numbers, which are divisible by 3,
# numbers that are not divisible by 2 and 3.

max_num = 10  
n = 1

while n < max_num:
    n+=1
    if n % 2 == 0:
        print("Even number: ", n)
    elif n % 3 == 0:
        print("Odd number is divisible by 3: ", n)
    elif n % 2 != 0 and n % 3 != 0:
        print("Number is NOT divisible by 2 and 3: ", n)
        