## https://nuancesprog.ru/p/10529/

## 1. __init__
## Инстанциирование: __new__ and __init__  += 2 in 1

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

# product = Product("Vacuum", 150.0)

## 2. Строковые представления: __repr__ and __str__ 

## Хотя оба метода должны возвращать строки, метод __repr__, как правило, предназначен для разработчиков,
## поэтому его цель  —  показать информацию об инстанциировании. 
## А вот метод __str__ рассчитан на обычных пользователей,
## в связи с чем в нем реализуется намерение отобразить что-то более информативное. 

## Метод __repr__ должен возвращать строку, показывающую, как может быть создан экземпляр. 
## Эта строка может быть передана в eval() для повторного создания экземпляра.

## Метод __str__ может вернуть более описательные данные экземпляра. 
# Этот метод используется функцией print() для отображения информации экземпляра !!!

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def __repr__(self):
#         return f"Product({self.name!r}, {self.price!r})"

#     def __str__(self):
#         return f"Product: {self.name}, ${self.price:.2f}"

# product1 = Product("Vacuum", 150.0)
# product2 = Product("Car", 13000.0)
# print(product1.__repr__())
# print(product2.__str__())
# print(Product)

# class Product:
#     cc = 0
#     l = []
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         Product.cc +=1
#         Product.l.append(self)
    
#     def li(self):
#         return Product.l

#     def __repr__(self):
#         return f"Product({self.name!r}, {self.price!r})"

#     def __str__(self):
#         return f"Product: {self.name}, ${self.price:.2f}"

# product1 = Product("Vacuum", 150.0)
# product2 = Product("Car", 13000.0)
# print(product1)
# print(Product.l)
# print(Product.cc)
# print(repr(product1))

## 3. Итерация: __iter__ and __next__  

## С помощью кода мы можем автоматизировать одну из ключевых операций - повторение некоторого действия,
## реализация которого подразумевает использование цикла for, 
## выступающего в роли логического процесса.
## Речь идет об итерируемом объекте, который можно использовать в этом цикле. 
## Ниже представлена самая простая форма цикла for: 

# for item in iterable:
#     # Далее следуют нужные операции 

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def __str__(self):
#         return f"Product: {self.name}, ${self.price:.2f}"

#     def __iter__(self):
#         self._free_samples = [Product(self.name, 0) for _ in range(3)]
#         print("Iterator of the product is created.")
#         return self

#     def __next__(self):
#         if self._free_samples:
#             return self._free_samples.pop()
#         else:
#             raise StopIteration("All free samples have been dispensed.")

# product = Product("Perfume", 5.0)
# for i, sample in enumerate(product, 1):
#     print(f"Dispense the next sample #{i}: {sample}")

# ## Iterator of the product is created.
# ## Dispense the next sample #1: Product: Perfume, $0.00
# ## Dispense the next sample #2: Product: Perfume, $0.00
# ## Dispense the next sample #3: Product: Perfume, $0.00

## Как показано выше, мы создаем список из объекта, содержащего free samples (бесплатные образцы)
## в методе __iter__, который образует итератор для экземпляра пользовательского класса.
## Чтобы произвести итерацию, мы реализуем метод __next__, предоставляя объект из списка free samples.
## Перебор элементов завершается в тот момент, когда заканчиваются free samples.

## 4. Контекстный менеджер: __enter__ and __exit__ 

## В целом, контекстные менеджеры  —  это объекты Python, которые управляют совместно используемыми ресурсами,
## например открывают и закрывают за нас файлы.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product: {self.name}, ${self.price:.2f}"

    def _move_to_center(self):
        print(f"The product ({self}) occupies the center exhibit spot.")

    def _move_to_side(self):
        print(f"Move {self} back.")

    def __enter__(self):
        print("__enter__ is called")
        self._move_to_center()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__ is called")
        self._move_to_side()

product = Product("BMW Car", 50000)
with product:     ### print("It's a very good car.")


## __enter__ is called
## The product (Product: BMW Car, $50000.00) occupies the center exhibit spot.
## It's a very good car.
## __exit__ is called
## Move Product: BMW Car, $50000.00 back.

## 5. Улучшенный контроль доступа к атрибутам: __getattr__ and __setattr__ 
## Метод __getattr__ вызывается при обращении к атрибутам экземпляра,
## а метод __setattr__  при их установке:

class Product:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        if item == "formatted_name":
            print(f"__getattr__ is called for {item}")
            formatted = self.name.capitalize()
            setattr(self, "formatted_name", formatted)
            return formatted
        else:
            raise AttributeError(f"no attribute of {item}")

    def __setattr__(self, key, value):
        print(f"__setattr__ is called for {key!r}: {value!r}")
        super().__setattr__(key, value)

product = Product("taBLe")
## __setattr__ is called for 'name': 'taBLe'
## product.name
## 'taBLe'
## product.formatted_name
## __getattr__ is called for formatted_name
## __setattr__ is called for 'formatted_name': 'Table'
## 'Table'
## product.formatted_name
## 'Table'