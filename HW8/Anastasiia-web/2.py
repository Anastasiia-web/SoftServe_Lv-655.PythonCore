# Task
# Create a class Human, everyone has a name, create a method in the class
# that displays a welcome message to a each person. Create a class method
# in the class that returns information that it is a species of "Homosapiens".
# And also in the class create a static method that returns an arbitrary message. 

class Human:
    our_species = 'Homosapiens'
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f"Hi {self.name}!"

    def type_of_human(self):
        return self.our_species

    @staticmethod
    def lol():
        gender = input("Enter your gender: ")
        if gender == 'male':
            return f"""

            \\\|||///

           (   * *   )
                ^
               ~~~
             \_____/

            Looks like 
              you:)
            """
        else:
            return f"""

           \\\\\|||////
         \\\  ~   ~  ///
        \\\    * *    ///
        \\\     ^     ///
        \\\  \_____/  ///
        \\\           ///

            Looks like 
              you:)
            """          


eva = Human('Eva')
adam = Human('Adam')
print(eva.greeting())
eva.type_of_human()
print(eva.lol())

print(adam.greeting())
adam.type_of_human()
print(adam.lol())
