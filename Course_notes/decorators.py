# def star(func):
#     def inner(*args, **kwargs):
#         print("_" * 30)       
#         func(*args, **kwargs)
#         print("_" * 30)
#     return inner


# @star
# def printer(msg):
#     print(msg)

# printer('Last news')

#_________

# Decorating Functions with Parameters

# def smart_divide(func):
#    def inner(a,b):
#       print("I am going to divide",a,"and",b)
#       if b == 0:
#          print("Whoops! Can not divide")
#          return
#       return func(a,b)
#    return inner

# @smart_divide
# def divide(a,b):
#     return a/b
# #_____________-

# <\ ^^^^^^^ /> 
# # tomato # 
# --meat– 
# ~ salad ~
#  <\ ______ />


def star(func):
    def inner(*args, **kwargs):
        print("<\ ^^^^^^^ />")       
        func(*args, **kwargs)
        print("<\ _______ />")
    return inner


@star
def printer(msg):
    print(msg)

printer(""" # tomato #
  - meat-
  ~ salad ~""")