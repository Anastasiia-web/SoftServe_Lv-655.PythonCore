# Напишіть скрипт, який обчислює площу прямокутника a*b, площу трикутника 0.5*h*a, 
# площу кола pi*r**2 і цей скрипт використати в іншому модулі, 
# в якому ми запитуємо користувача площу якої фігури він хоче обчислити. 

# (для виконання завдання необхідно імпортувати  модуль math, 
# а з нього функцію pow() та значення змінної пі, 
# модуль1, який містить три функції для знаходження площ, 
# модуль2, в якому імпортований модуль1 і виконується основна логіка програми).

import module1

def user_makes_choice():
    user_choice = input("The area of ​​which figure you want to calculate? Enter: 1 for rectangle. 2 for triangle. 3 for circle ")

    if user_choice == '1':
        side_1 = float(input("Enter side 1 length: "))
        side_2 = float(input("Enter side 2 length: "))           
        print(module1.rectangle_area(side_1, side_2))
    elif user_choice == '2':
        side = float(input("Enter side: "))
        height = float(input("Enter width: "))
        print(module1.triangle_area(side, height))
    elif user_choice == '3':
        radius = float(input("Enter radius: "))
        print(module1.circle_area(radius))
    else:
        print("Try again please!")
        user_makes_choice()

user_makes_choice()
