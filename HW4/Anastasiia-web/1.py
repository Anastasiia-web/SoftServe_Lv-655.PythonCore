# Factorial
# Write a script that will calculate the factorial of the entered number without using recursion

n=int(input("Enter number: "))

fact_num=1

while(n>0):
    fact_num = fact_num * n
    n = n-1
print("Factorial of the number is:", fact_num)
  

  
# https://www.sanfoundry.com/python-program-find-factorial-number-without-recursion/  
# A factorial variable is initialized to 1.
# A while loop is used to multiply the number to the factorial variable and then the number is decremented each time.
# This continues till the value of the number is greater than 0.

# My drafts
# 1.

#a = 4

# while a<6:
    # print('hi', a)
    # a +=1
# else: 
    # print('no', a)

# 2.
# b = int(input('Give a number please '))

# for i in (range(b)):
#     print(i*i)
# else:
#     print('The end')

# 3. 
# h = 9
# i = int(input('Your number?'))
# if h in range(i):
#     print(h*h)
#     i +=1
# else:
#     print('hi')

# 4. 
# if score >= 90: 
#        letter = 'A' 
# elif score >= 80: 
#        letter = 'B' 
# elif score >= 70: 
#        letter = 'C' 
# elif score >= 60: 
#        letter = 'D‘
# else: letter = 'F' 

# 5. Ternary Operator: statement() if condition else statement()
# weather = "raining“

# print("Open Your umbrella" if weather == "raining" else "Wear your cap")
