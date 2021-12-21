# ##       WORKING my solution                          TEST 16. Drag & drop function: Create 2 lists with 'e' and without at the end of words
## WORKING my solution  
# color_list = ['red', 'orange', 'blue', 'brown', 'green', 'white']
# e = list(filter(lambda x: x[-1] == 'e', color_list))
# print(e)
# v = list(filter(lambda y: y[-1] != 'e', color_list))
# print(v)
######################

##  WORKING !!!            my solution                                  1. Вычислить сумму (в списке списка)                 

# list_first = [[11, 2, 3], [44,5,6], [10,1,2], [17, 8, 6]]

# list_not_nested = [element for sub_list in list_first for element in sub_list]       # раскрываем нестед лист

# print(list_not_nested)    # [11, 2, 3, 44, 5, 6, 10, 1, 2, 17, 8, 6]

# a = sum(list_not_nested)
# print(a)      # 115



##################
##   WORKING my solution                         TEST 7. drag & drop function return dictionary key=symbols, values=count

# word = 'hhjuijjj'
# word_list = list(word)
# values_list = []

# for i in word_list:
#     p = word_list.count(i)
#     values_list.append(p)
# print(values_list)

# w = dict(zip(word_list, values_list))
# print(w)
########   WORKING using function с условием, но моим)
# def count_symbols():
#     word = 'hhjuiiiijjj'
#     result = {}

#     if type(word) == str:
#         word_list = list(word)
#         values_list = []

#         for i in word_list:
#             p = word_list.count(i)
#             values_list.append(p)

#         result = dict(zip(word_list, values_list))
#         return(result)
#     else:
#         return False

# print(count_symbols())
############# 

# ########   WORKING using function  без условий
# def count_symbols():
#     result = {}

#     word_list = list('hhjuiiiijjj')
#     values_list = []

#     for i in word_list:
#         p = word_list.count(i)
#         values_list.append(p)

#     result = dict(zip(word_list, values_list))
#     print(result)

# count_symbols()

# ###############

# def count_symbols():    # working as in test for condition     !!! NEEDS TO BE SOLVED ACCORDING TO THE INSTRACTIONS
#     word = 'hhjuiiiijjj'
#     result = {}
#     for symbol in word:
#         result[word] = symbol.count(word)
#         result[symbol] = word.count(symbol)
#         return result
#     if type(word) != str: 
#         return False
# print(count_symbols())

################################################################
######################  interesting about copy!!  copies if dict and srt NOT changed !!! list's copies changed

# ##                                                                           TEST 9. What gets printed?
# kvps = {'1': 1, '2': 2}
# theCopy = dict(kvps)
# print(kvps)       # {'1': 1, '2': 2}
# print(theCopy)    # {'1': 1, '2': 2}

# kvps['1'] = 5     # theCopy of dictionary is NOT changed !!!!
# print(kvps)       # {'1': 5, '2': 2}
# print(theCopy)    # {'1': 1, '2': 2}
# # sum = kvps['1'] + theCopy['1']
# # print(sum)                                                # answer : 6 

# list_1 = ['1', '2']
# list_2 = list_1
# print(list_1)    # ['6', '2']
# print(list_2)    # ['6', '2']

# list_1[0] = '6'  # theCopy of list is changed !!!!

# print(list_1)    # ['6', '2']
# print(list_2)    # ['6', '2']

# str_1 = '1hhhh'
# str_2 = str_1
# print(str_1)    # 1hhhh
# print(str_2)    # 1hhhh

# str_1 = 'W'  # theCopy of str is NOT changed !!!!

# print(str_1)    # W
# print(str_2)    # 1hhhh

################################
# print(0.2+0.2)   # 0.4

########
# # ##                                                                                      TEST 30. What gets printed?
# print("\x48\x49!")                       # answer :  HI!
# # 2
# # They are called hexadecimal escape sequences.
# # If you are using firefox or chrome, they can turn it into a text if you just copypaste a string 
# # like '\x48\x49' to the their console. But you could also use this http://jsfiddle.net/HHfdp/show/
# # find out more about these in the Python documentation for String Literals.

########
# # ##                                                                                      TEST 31. What gets printed?
# boxes = {}     # print(len(crates[boxes]))    # answer : TypeError: unhashable type: 'dict'
# jars = {}
# crates = {}

# boxes['cereal'] = 1
# boxes['candy'] = 2  # {'cereal': 1, 'candy': 2}
# print(boxes)  
# jars['honey'] = 4   # {'honey': 4}
# print(jars)
# crates['boxes'] = boxes # {'cereal': 1, 'candy': 2}
# crates['jars'] = jars

# # print(len(crates[boxes]))                # answer : TypeError: unhashable type: 'dict' (You're trying to use a dict as a key to another dict or in a set .
#                                              That does not work because the keys have to be hashable.)

# print(crates) # {'boxes': {'cereal': 1, 'candy': 2}, 'jars': {'honey': 4}}

## Вы пытаетесь использовать dict в качестве ключа к другому dict или в set. Это не работает,
## потому что ключи должны быть хешируемыми. Как правило, только неизменяемые объекты
## (строки, целые числа, float, frozensets, кортежи неизменяемых) являются хешируемыми (хотя возможны исключения).
## !!! как обойти это https://overcoder.net/q/69071/typeerror-unhashable-%D1%82%D0%B8%D0%BF-dict