# Factorial
n = int(input("?: "))
fact = 1
while n > 0:
    fact = fact *n
    n = n-1
print(fact)

# Fibonacci
inp = int(input("?: "))
a, b = 0, 1
while b <= inp:
    print(b)
    a, b = b, a + b

#########

l = 'hjkjlj'                              # изменила каждый элемент в строке через новый список и обратно в строку
h = []
for i in l:
    p = i+'y'
    h.append(p)
print("".join(h))


o = ['kj','g']                                      # отфильтровать слово в списке  filter
s = list(filter(lambda c: c =='g',o))
print(s)

o.remove('g')                                       # удалем элемент из списка
print(o)

############

## enumerate !!!  https://realpython.com/python-enumerate/
## аналогично:                             # присваиваем списку индекс
values = ["a", "b", "c"]
index = 0
for value in values:
    print(index, value)
    index += 1
## аналогично:
for count, value in enumerate(values):
    print(count, value)
## аналогично:
for count, value in enumerate(values, start=1):
    print(count, value)
