# Write a program that calculates the square of ​​a rectangle, triangle and circle 
# (write three functions to calculate the square, and call them in the main program depending on the user's choice).

# 1. square of ​​a rectangle
side_a = float(input('Enter rectangle side A length? '))
side_b = float(input('Enter rectangle side B length? '))

rectangle_square = round((side_a*side_b), 2)
print('Rectangle square: ', rectangle_square)

# 2. square of ​​a triangle S=(a/2)*h

base_side_c = float(input('Enter triangle base side C length? '))
hight_h = float(input('Enter triangle hight length? '))

triangle_square = round((base_side_c/2*hight_h), 2)
print('Triangle square:', triangle_square)

# 3. square of ​​a circle

def square_circle_calculating():
    p = 3.14
    user_choice = int(input("Circle Square using: Enter '1' - radius. Enter '2' - diametr. Enter '3' - circumference. Your choice: "))
    if user_choice == 1 or user_choice == 2 or user_choice == 3:
        if user_choice == 1:
            radius = float(input('Enter radius length: '))
            radius_circle_square = round((p * (radius * radius)), 2)
            print('Circle square: ', radius_circle_square)
        elif user_choice == 2:
            diametr = float(input('Enter diametr length: '))
            diametr_circle_square = round((p * (diametr * diametr)/4), 2)
            print('Circle square: ', diametr_circle_square)
        elif user_choice == 3:
            circumference = float(input('Enter circumference length: '))
            circumference_circle_square = round((circumference * circumference/(4*p)), 2)
            print('Circle square: ', circumference_circle_square)
    else:
        print("Choose again please!")
        square_circle_calculating()

square_circle_calculating()





# My draft

# 3. square of ​​a circle 
# p = 3.14
# radius = float(input('Enter radius length?'))
# diametr = float(input('Enter diametr length?'))
# circumference = float(input('Enter circumference length?'))

# radius_circle_square = round((p * (radius * radius)), 2)
# print(radius_circle_square)

# diametr_circle_square = round((p * (diametr * diametr)/4), 2)
# print(diametr_circle_square)

# circumference_circle_square = round((circumference * circumference/(4*p)), 2)
# print(circumference_circle_square)


# double = lambda x: x*2
# print(double(5))

# my_list = [2,3,8,7,1]
# double_list = list(map(lambda x: x*2, my_list))
# print(double_list)
# print(type(my_list))

# filtered_list = list(filter(lambda x: x%2==0, my_list))
# print(filtered_list)

# https://premierdevelopment.ru/on-line-kalkulyator-raschet-ploshchadi-treugolnika.html
# https://allcalc.ru/node/18
