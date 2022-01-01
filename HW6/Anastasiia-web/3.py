# Task3. Write a function that calculates the number of characters included in a given string

def char_number():
    string = input('Enter a string: ')
    string_without_spaces = string.replace(" ", "")
    print('The number of characters in a string: ', len(string_without_spaces))

char_number()

# Option using one more variable

# def char_number():
#     string = input('Enter a string: ')
#     string_without_spaces = string.replace(" ", "")
#     string_length = len(string_without_spaces)
#     print(string_length)

# char_number()
