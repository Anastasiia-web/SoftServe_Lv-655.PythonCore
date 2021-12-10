# TASK 2
n = 1230                                                               # Задано чотирицифрове натуральне число
print(n)

# 1. Знайти добуток цифр цього числа
digit_1 = int(n/1000)
digit_2 = int(n/100)%10
digit_3 = int(n/10)%(int(n/100))
digit_4 = n%(int(n/10))                                                

digits_multiplication = int(n/1000) * (int(n/100)%10) * (int(n/10)%(int(n/100))) * (n%(int(n/10)))

print(digits_multiplication)
print(digit_1)
print(digit_2)
print(digit_3)
print(digit_4)

# 2. Записати число в реверсному порядку
# Option 1
print(digit_4,digit_3,digit_2,digit_1)     # ? There are spaces in between digits. How to get rid of them?

# Option 2
reverse_number = digit_4, digit_3, digit_2, digit_1      # ? Is there a way how to join tuple?          
print(reverse_number)

# Option 3
input_number_for_reversing = input('What is a number to reverse? ')
reversed_number = input_number_for_reversing[::-1]

print('Reversed number is', reversed_number)

# Option 4

n = 900         # ? Цикл обрежет нули. Как этого избежать?
m = 0
while n>0:
    m = m*10 + n%10
    n = n//10
print(m)

# Option 5
n1 = input("Введите целое число: ")        # n2 - строка, как корректно перевести в число?
n_list = list(n1)
print(n_list)           #['6','7']
n_list.reverse()
n2 = "".join(n_list)
print('"Обратное" ему число:', n2)

# Option 6
n1 = input("Введите целое число: ") 
n2 = n1[::-1] 
print('"Обратное" ему число:', n2)

# Option 7
k='500'                                    # result - строка, как корректно перевести в число?
result = ""
for i in reversed(k): 
    result += i
print(result)

# Option 8
s='900'                                    # result1 - строка, как корректно перевести в число?
result1=""
for i in range(len(s)-1, -1, -1):
    result1 += s[i]
print(result1)
