

import re
 
# s = input('Stupid! : ')                     #  work
# nums = re.findall(r'\d+', s)   #  work

# nums = [int(i) for i in nums]   # work

# f = nums[0]*nums[1]*nums[2]  #  work
# print(f)
#_____________

# def inputSides():       
#         sides_a_b = input('Enter 2 numbers separated by coma: ')
#         try:
#             # # a = re.findall(r'\-', sides_a_b)
#             # if "-" in sides_a_b:
#             print("Y!")
#                 # inputSides()
#         except:
#             if "-" in sides_a_b:
#             # if "-" not in sides_a_b:
#                 # nums = re.findall(r'\d+', sides_a_b)   #  work
#                 # nums = [int(i) for i in nums]   # work
#                 # f = nums[0]*nums[1] #  work
#                 print("g")
# inputSides()


# # inp = input("?: ")

# def divide():
#     inp = input("?: ")
#     inp != 'y'

#     while True:
#         try:
#             print("h")
#             break
#         except:
#             print("Error case")
 
# divide()

# while True:
#     x = int(input())

#     try:
#         result = 1 / x
#     except:
#         print("Error case")
#         exit(0)


# try: 
#     a = int(input("Enter your number: ")) 
#     if a < 4: 
#         b = a/(a-3)         # throws ZeroDivisionError for a = 3 
    
#     if a >= 4:      
#         print("Value of b = ", b)    # throws NameError 

# # note that braces () are necessary here for multiple exceptions 
# except ValueError:
#     print("Value Error!")
# except NameError: 
#     print("NameError!")
# except ZeroDivisionError:
#     print("ZeroDivisionError!")
# except:
#     print("Error!")


# # def divide():
#     inp = input("?: ")

#     try:
#     if inp == "p":
#         print("Value")
#     except:
#     if inp != "p":
#         print('Non-numeric input detected.')

# # divide()
# inp = input("?: ")
# try:
#     if inp == "8":
#         print("j")
# except:
#     print("An eion occurred")

# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")

# inp = input("?: ")

# def check():
#     inp = input("?: ")
#     if inp == '0':
#        print("Sorry, no numbers below zero")
#        check()
#     else:
#         print("ok")
# check()
def ii(i):
    while i > 0:
        try:
            n = i*2
            print(n)
            break
        except:
            print('O my God')
            ii(6)
ii(-6)


# try:
#     # Some Code
# except:
#     # Executed if error in the
#     # try block

        # try:
        #     # a = re.findall(r'\-', sides_a_b)
        #     if "-" in sides_a_b:
        #         print("Your number is negative, please try again!")