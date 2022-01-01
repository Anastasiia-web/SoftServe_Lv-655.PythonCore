# Your collegue wrote an simple loop to list his favourite animals. 
# But there seems to be a minor mistake in the grammar, which prevents the program to work. Fix it! :)
# If you pass the list of your favourite animals to the function, you should get the list of the animals 
# with orderings and newlines added.
# For example, passing in:
# animals = [ 'dog', 'cat', 'elephant' ]
# will result in:
# list_animals(animals) == '1. dog\n2. cat\n3. elephant\n'

# Loop with mistake
# def list_animals(animals):
#     list = ''
#     for i in range(animals):
#         list += str(i + 1) + '. ' + animals[i] + '\n'
#     return list

# Solution

def list_animals(animals):
    list = ''
    for i in range(len(animals)):                        # adding "len"
        list += str(i + 1) + '. ' + animals[i] + '\n'
    return list

# Best practice

# Option 1

def list_animals(animals):
    return ''.join('{0}. {1}\n'.format(i + 1, x) for i, x in enumerate(animals))

# Option 2

def list_animals(animals):
  return ''.join(f'{i}. {animal}\n' for i, animal in enumerate(animals, 1))

# Option 3

def list_animals(animals):
    list = ''
    i=0
    for elements in animals:
        list += str(i + 1) + '. ' + elements + '\n'
        i+=1
    return list

# Option 4

def list_animals(animals):
    string = ''
    for i, animal in enumerate(animals, start=1):
        string += f'{i}. {animal}\n'
    return string

# Option 5

def list_animals(animals):
    return ''.join(str(i + 1) + '. ' + animals[i] + '\n' for i in range(0, len(animals)))

# Option 6

def list_animals(animals):
    u = ""
    i=0
    while i < len(animals):
        s=str(i + 1)
        s=s+'. '+ animals[i]
        s=s+ '\n'
        u = u + s
        i=i+1
    return u
