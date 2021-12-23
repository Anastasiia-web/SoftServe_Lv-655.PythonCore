# ###  WORKING my solution                 Test task 1 : make an array of indexes of "None" value out of given array
# given_list = [4,"a", 5, "a"]

# enumerated_list = list(enumerate(given_list))  # [(0, 4), (1, 'a'), (2, 5), (3, 'a')]

# result = []
# for key, value in enumerated_list:
#     if value == "a":
#         result.append(key)
# print(result)                  # answer :  [1, 3]

### WORKING my solution   Test task 2 : выделить чётные и нечётные, посчитать и соединить в дикт {"even": n_e, "odd": n_o}
# inp= str(234)               # 234
# n = list(inp)               # ['2', '3', '4']
# di = [int(i) for i in n]    # [2, 3, 4]     # синтаксич сахар
# n_e = list(filter(lambda i: i%2 == 0, di))   # answer : [2, 4]
# n_o = list(filter(lambda i: i%2 == 1, di))   # answer : [2, 4]
# how_many_e = 0
# for i in n_e: how_many_e += 1          # 2
# how_many_o = 0
# for i in n_o: how_many_o += 1     # 1

# result = {"even": how_many_e, "odd": how_many_o}   # {'even': 2, 'odd': 1}

### WORKING my solution                                              Test task 3 : fibonacci
# a, b = 0, 1

# while b <5:
#     print(b)
#     a, b = b, a+b

#####  Why this answer!!!                                                 Test task 4 : what's the output? 

## !!! ПОВЕРХНОСТНАЯ КОПИЯ 1 и 3 списков = 1 айди, второму обнулили список перед входом в функцию - [] !!!
##             __dir__) # пробить айди объектов !!!

# def extendList(item, list=[]):
#     list.append(item)
#     return list

# list1 = extendList(11)      
# list2 = extendList(156,[])  
# list3 = extendList('c')      

# print(list1) 
# print(list2)
# print(list3)

# print(list1.__dir__) # пробить айди объектов !!!
# print(list2.__dir__) # пробить айди объектов !!!
# print(list3.__dir__) # пробить айди объектов !!!

# print("list1 = {}".format(list1))
# print("list2 = {}".format(list2))
# print("list3 = {}".format(list3))

###### how from input get even numbers  НАЙТИ БАГ НА ДОСУГЕ))
# inp= str(234)               # 234
# n = list(inp)               # ['2', '3', '4']
# di = [int(i) for i in n]    # [2, 3, 4]     # синтаксич сахар
# n_e = list(filter(lambda i: i%2 == 0, di))   # answer : [2, 4]
# v = list(enumerate(di))   #  [(0, 2), (1, 3), (2, 4)]

# val_e = []
# for key, value in v:
#     if value%2 ==0:
#         val_e.append(key)
# print(val_e)                #  [0, 2]  #  получили чётные 

# coun_e = 0
# for i in val_e:
#     coun_e +=1
# print(coun_e)                # посчитали чётные

# val_o = []

# for key, value in v:
#     if value%2 ==0:
#         val_o.append(key)
# print(val_o)                #  [0, 2]  #  получили чётные 

# coun_o = 0
# for i in val_o:
#     coun_o +=1
# print(coun_o)                # посчитали чётные

# res_n =[coun_e, coun_o]
# print(res_n)
###############################################
# listl = [7,8]

# new_list2 = list(filter(lambda x: (x%2 == 0), listl))     # отбираем чётные lambda !!! 
#                                                           # Фильтру нужно 2 аргумента( как , что фильтруем)
# print(new_list2)


#########

############

### https://younglinux.info/algorithm/fibonacci
### https://all-python.ru/raznoe/chisla-fibonachchi.html
### https://habr.com/ru/post/261159/


# list_value



#########
#### https://www.activestate.com/resources/datasheets/tkinter-cheatsheet-tips-and-tricks-to-create-your-user-interface/
## python cheat sheet Web-UI for Python

#  как работать с Гуи через Тринкет:
# https://realpython.com/python-gui-tkinter/
# with
# Check Your Understanding
# Expand the code block below for an exercise to check your understanding:

### 2 тест
# valid IP addresses according to IPv4 protocol?

# An IP address is a set of numbers that identify your computer on a network.
# IPV4,
# the traditional numbering scheme, uses four integers ranging
# from zero to 255 and set apart by periods. For example, 
# "204.120.0.15" is a valid IPV4 address.
# потому что от 0 до 255 и цифры поделены на 4 части

# Reserved Addresses
# Networks set aside certain combinations for housekeeping and testing, such as the extreme values,
# "0.0.0.0" and "255.255.255.255." Another number, "127.0.0.1" 
# is called the "localhost;"  =>  would be invalid as have special meanings!
# every computer on a network refers to itself as this address

# https://smallbusiness.chron.com/ip-address-invalid-68006.html

# DHCP Assignment Problems
# A network service called Dynamic Host Configuration Protocol offers a convenient way to 
# automatically assign IP addresses to computers joining a network. For example, as you return home from work,
# your smartphone picks up
# the Wi-Fi signal from your home network and
# the network's DHCP service gives the phone an IP address. 

# Address Conflicts
# On a given network, every IP address must be unique.
# Two computers cannot both have the address "192.168.0.110."

# Address Conflicts

#####################
# коды состояний : руководство по REST API

# * 403: Forbidden   
# * 404: Not Found

# https://restapitutorial.ru/httpstatuscodes.html  !!! ЧИТАТЬ

# Код ответа (состояния) HTTP показывает, был ли успешно выполнен определённый HTTP запрос.
# Коды сгруппированы в 5 классов:

# Информационные 100 - 199
# Успешные 200 - 299
# Перенаправления 300 - 399
# Клиентские ошибки 400 - 499
# Серверные ошибки 500 - 599

###################
# Test question : port 80                          READ !!! https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D1%80%D1%82_
# (%D0%BA%D0%BE%D0%BC%D0%BF%D1%8C%D1%8E%D1%82%D0%B5%D1%80%D0%BD%D1%8B%D0%B5_%D1%81%D0%B5%D1%82%D0%B8)

# Наличие значения по умолчанию полезно именно потому, что вам не нужно вводить его в веб-браузер с помощью URI

# Порт (англ. port) — целое неотрицательное число, записываемое в заголовках протоколов транспортного уровня
# сетевой модели OSI (TCP, UDP, SCTP, DCCP).

# По умолчанию в протоколе HTTP используется порт 80, а в протоколе HTTPS — порт 443.
# URL вида
# http://www.example.com:8080/path/ указывает,
# что веб-ресурс обслуживается веб-сервером на порту 8080.



# ###  WORKING !!!                               Test task : make an array of indexes of "None" value out of given array
# lis = [4,"a", 5, "a"]
# l = list(enumerate(lis))  # [(0, 4), (1, 'a'), (2, 5), (3, 'a')]
# x = []
# for key, value in l:
#     if value == "a":
#         x.append(key)
# print(x)                  # answer :  [1, 3]

############

# ind = lis.index("a")
# print(ind)

# for i in l:
#     d = l.index("a")
# print(l)

# i = "a"
# p = []
# for i in lis:
#     p.append(lis.index(i))
# print(p)

###########

# d = 45
# print(d.__dir__)                 # ID ОБЪЕКТА !!!

###########