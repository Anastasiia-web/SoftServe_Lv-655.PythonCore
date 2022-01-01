# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings:
# name + " plays banjo" 
# name + " does not play banjo"

def are_you_playing_banjo(name):

    return name + " plays banjo" if name[0] == 'r' or name[0] == 'R' else name + " does not play banjo"

print(are_you_playing_banjo('Roma'))

# the same as

# def are_you_playing_banjo(name):

#     if name[0] == 'r' or name[0] == 'R':
#         return name + " plays banjo"
#     else:
#         return name + " does not play banjo"

# print(are_you_playing_banjo('Roma'))


# Best practice

def areYouPlayingBanjo(name):

    return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo"

print(areYouPlayingBanjo('Roma'))

# Notes practicing formating

x1, y1 = 1, 11
x2, y2 = 2, 22
result = 'result'

print(f"distance between {(x1,y1)} and {(x2,y2)} is {result}")

print("{} is not equal to {} as a {}".format(x1, y1, result))

print("distance between", (x1,y1), "and", (x2,y2), "is", result)
