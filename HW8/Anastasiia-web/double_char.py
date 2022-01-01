# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
# double_char("String") ==> "SSttrriinngg"
# double_char("Hello World") ==> "HHeelllloo  WWoorrlldd"
# double_char("1234!_ ") ==> "11223344!!__  "

def double_char(s):
    symbols_list = list(''.join(s))
    doubled_symbols = list(map(lambda i: i*2, symbols_list))
    return ''.join(doubled_symbols)

double_char("Hello World")

# Best practice

# s = 'dgh'

def double_char(s):
    return ''.join(c * 2 for c in s)
