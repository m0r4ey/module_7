# Режимы открытия файлов
from pprint import pprint


class Product():

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop():
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r').read()
        return file

    def add(self, *products):
        for product in products:
            if self.get_products().count(f'{product}') == 0:
                file = open(self.__file_name, 'w')
                file.write(f'\n{product}')
                file.close()
            else:
                print(f'Продукт {product} уже есть в магазине.')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
