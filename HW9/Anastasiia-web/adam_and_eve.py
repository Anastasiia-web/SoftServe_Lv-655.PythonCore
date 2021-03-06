# According to the creation myths of the Abrahamic religions, 
# Adam and Eve were the first Humans to wander the Earth.

# You have to do God's job. The creation method must return an array of length 2 containing objects 
# (representing Adam and Eve). The first object in the array should be an instance of the class Man. 
# The second should be an instance of the class Woman. Both objects have to be subclasses of Human. 
# Your job is to implement the Human, Man and Woman classes.

def God():
    return [Man(), Woman()]

class Human(object):
    pass

class Man(Human):
    pass
    
class Woman(Human):
    pass

# Best Practice
# Option 1

def God():
    return [ Man("Adam"), Woman("Eva") ]

class Human:
   def __init__( self, name ):
      self.name = name

class Man( Human ):
   def __init__( self, name ):
      self.name = name

class Woman( Human ):
   def __init__( self, name ):
      self.name = name


# Option 2

class Human(object):
    def __init__(self):
        pass

class Man(Human):
    def __init__(self, name):
        self.name = name

class Woman(Human):
    def __init__(self, name):
        self.name = name

def God():
    adam = Man('Adam')
    eva = Woman('Eva')
    return [adam, eva]
    