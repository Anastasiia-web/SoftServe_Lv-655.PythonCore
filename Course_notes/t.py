# def extendList(item, list=[]):
#     list.append(item)
#     return list

# list1 = extendList(11)
# list2 = extendList(156,[])
# list3 = extendList('c')

# print("list1 = {}".format(list1))
# print("list2 = {}".format(list2))
# print("list3 = {}".format(list3))

############
# def fibo(n):
#     for i in range(0,n-1):
#         f_n.append(f_n[i]) + f_n(i-1)


#     return f_n

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
