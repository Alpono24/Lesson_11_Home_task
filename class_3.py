#1111111111111111111111111111111111111111111111111111111111111111111
#class Computer:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.__price = price
#
#     #getter
#     def get_price(self):
#         return self.__price
#     #setter
#     def set_price(self, value):
#         if value > 0:
#             self.__price = value
#         else:
#             print('Price cannot be negative')
#     def show_info(self):
#         print(f'{self.brand}, price: {self.__price}')
#
#
# pc = Computer('Acer', 2590)
# pc.show_info()
# print(pc.get_price())
# pc.set_price(100)
# print(pc.get_price())

#1111111111111111111111111111111111111111111111111111111111111111111
# class Computer:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.__price = price
#
#     #getter
#     @property
#     def price(self):
#         return self.__price
#     #setter
#
#     @price.setter
#     def price(self, value):
#         if value > 0:
#             self.__price = value
#         else:
#             print('Price cannot be negative')
#
#     def show_info(self):
#         print(f'{self.brand}, price: {self.__price}')
#
#
# pc = Computer('Acer', 2590)
# pc.show_info()
# print(pc.price)
# pc.price = 2000
# print(pc.price)


#1111111111111111111111111111111111111111111111111111111111111111111

# class Computer:
#     def __init__(self, price, tax):
#         self.__price = price
#         self.__tax = tax
#
#     @property
#     def full_price(self):
#         return self.__price * (1+self.__tax)
#
# pc = Computer(price=100, tax=0.20)
# print(pc.full_price)


# pc.full_price = 2000 #XXXXXXXXXXXXXXXXXXXXXXXXX
#1111111111111111111111111111111111111111111111111111111111111111111
