## Списки
# 1. Задача «Удалить элемент»
# Дан список из чисел и индекс элемента в списке k. Удалите из списка элемент с индексом k, 
# сдвинув влево все элементы, стоящие правее элемента с индексом k.
# Программа получает на вход список, затем число k. Программа сдвигает все элементы, 
# а после этого удаляет последний элемент списка при помощи метода pop() без параметров.

numbers_list = [2,3,4,5,6,7,9]
del numbers_list[given_index_k]
numbers_list.pop()

# 2. Задача «Больше предыдущего»
# Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.

# Option 1: вывод списком

numbers_list = [2,8,4,5,6,7,1]
new_list = []
for i in range(1, len(numbers_list)):
    if numbers_list[i] > numbers_list[i - 1]:
        new_list.append(numbers_list[i])
print(new_list)

## Option 2Ж вывод элементов по очереди

for i in range(1, len(numbers_list)):
    if numbers_list[i] > numbers_list[i - 1]:
        print(numbers_list[i])

# 3. Задача «Наибольший элемент»
# Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке. 
# Если наибольших элементов несколько, выведите индекс первого из них.

numbers_list = [2,8,4,5,6,7,1]

max_number = max(numbers_list)
max_number_index = numbers_list.index(max_number)

print(max_number)
print(max_number_index)

# 4. Задача «Переставить min и max»
# В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.

numbers_list = [2,8,4,5,6,7,1]

min_number = min(numbers_list)
max_number = max(numbers_list)
min_number_index = numbers_list.index(min_number)
max_number_index = numbers_list.index(max_number)
numbers_list[min_number_index] = max_number
numbers_list[max_number_index] = min_number

print(numbers_list)
