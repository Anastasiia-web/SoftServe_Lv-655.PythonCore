# Consider an array/list of sheep where some sheep may be missing from their place.
# We need a function that counts the number of sheep present in the array (true means present).
# Hint: Don't forget to check for bad values like null/undefined

def count_sheeps(sheep):
    return len(sheep) - sheep.count(False) - sheep.count(None)

print(count_sheeps([True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, None, True ]))


# Option using variable

def count_sheeps(sheep):
    not_sheep = sheep.count(False)
    non_to_count = sheep.count(None)
    sheeps_number = len(sheep) - not_sheep - non_to_count
    return sheeps_number

print(count_sheeps([False, None ,True]))

# My draft
# fruits = ['apple', 'banana', 'cherry']

# x = fruits.count("cherry")
# print(x)
