# Create an employee class. Each employee has characteristics such as name and salary. 
# The class should have a counter that calculates the total number of employees, 
# as well as a method that prints the total number of employees 
# and a method that displays information about each employee in particular, namely the name and salary.

#In addition to creating a class, display information about the base classes 
#from which the employee class is inherited (__base__), the class namespace (__dict__), 
#the class name (__name__), the module name in which the class is defined (__module__), 
#the documentation bar (__doc__) 

class Employee:
    """
    An employee class
    """
    count_employees = 0

    def __init__(self, name, salary = 0):
        self.name = name
        self.salary = salary
        Employee.count_employees +=1

    def __del__(self):
        Employee.count_employees -=1


    def total_employees_number():
        print(f"Total number of employees: {Employee.count_employees}")

    def employee_info(self):
        print(f"""Employee name: {self.name}
       salary: {self.salary}""")

emp_1 = Employee('Oliver', 2)
emp_2 = Employee('John', 5)

Employee.total_employees_number()
   
emp_1.employee_info()
emp_2.employee_info()

print(Employee)
print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
