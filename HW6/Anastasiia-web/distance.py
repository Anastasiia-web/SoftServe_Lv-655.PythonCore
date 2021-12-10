# Given two ordered pairs calculate the distance between them.
# Round to two decimal places. This should be easy to do in 0(1) timing.

def distance(x1, y1, x2, y2):
    result = round(((((x2-x1)**2)+((y2-y1)**2))**0.5), 2)
    return result

distance(1, 1, 0, 0)

# Option with printing the result

def distance(x1, y1, x2, y2):
    result = round(((((x2-x1)**2)+((y2-y1)**2))**0.5), 2)
    print("distance between",(x1,y2),"and",(x1,y2),"is: ", result)

distance(1, 1, 0, 0)
