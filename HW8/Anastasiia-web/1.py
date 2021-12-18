# Create a polygon class and a rectangle class 
# that inherits from the polygon class and finds the square of rectangle. 
# Example:
# class Polygon:
#     def __init__(self, no_of_sides):
#         self.n = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]

#     def inputSides(self):
#         self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

#     def dispSides(self):
#         for i in range(self.n):
#             print("Side",i+1,"is",self.sides[i])

# class Triangle(Polygon):
#     def __init__(self):
#         super().__init__(3)
#     def findArea(self):
#         a, b, c = self.sides
#         s = (a + b + c) / 2
#         area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
#         print('The area of the triangle is %0.2f' %area)

# t = Triangle()
# t.inputSides()
# t.dispSides()
# t.findArea()

#___________________________

# Option to calculate only triangle area

class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(3)]

    def dispSides(self):
        for i in range(3):
            print("Side",i+1,"is",self.sides[i])

class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)
    def findArea(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)

t = Triangle()
t.inputSides()
t.dispSides()
t.findArea()

# Option to calculate only rectangle area

class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(2)]

    def dispSides(self):
        for i in range(2):
            print("Side",i+1,"is",self.sides[i])

class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)  
    def findArea(self):
        a, b = self.sides
        area = a*b
        print(f'The area of the rectangle is {area}')

r = Rectangle()
r.inputSides()
r.dispSides()
r.findArea()


# Option for user input separated by coma or space 

import re

class Polygon:
    def __init__(self, sides_a_b):
        self.sides = sides_a_b

    def inputSides(self):       
        sides_a_b = input('Enter 2 numbers separated by coma or space: ')
        nums = re.findall(r'\d+', sides_a_b)   
        self.sides = [int(i) for i in nums]  

class Rectangle(Polygon):
    def __init__(self):
        super().__init__(self)  
    def findArea(self):
        a, b = self.sides
        area = a*b
        print(f'The area of the rectangle is {area}')

r = Rectangle()
r.inputSides()
r.findArea()
