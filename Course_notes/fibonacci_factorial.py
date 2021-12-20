#  Print Fibonacci numbers up to the entered number n, using cycles. 
# 1
a, b, = 0, 1
end_of_loop = input('Enter a number :')

while b <= 55:
    print(b)
    a, b = b, a + b
    if b == end_of_loop:
        break
print('This is the end of loop)')

# 2
a, b, = 0, 1

while b <= 55:
    print(b)
    a, b = b, a + b

# 3

# Use 'Ctrl + C'to stop the loop))

a, b, = 0, 1

while b > 0:
    print(b)
    a, b = b, a + b

    

# My draft

# Чи́сла Фибона́ччи — элементы числовой последовательности 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 
# 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, …, в которой первые два числа равны 0 и 1, 
# а каждое последующее число равно сумме двух предыдущих чисел.

# https://www.youtube.com/watch?v=MxQ9_pg0TKA
# https://all-python.ru/osnovy/tsikly.html


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
