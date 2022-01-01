# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

# Option 1

def bool_to_word(boolean):
    return 'Yes'if boolean == True else 'No'

bool_to_word(False)

# Option 2

def bool_to_word(boolean):
    if boolean == True:
        return 'Yes'
    else:
        return 'No'

bool_to_word(True)
