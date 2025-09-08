#1111111111111111111111111111111111111111111111111111111111111111111
# class Car:
#     car_count = 0
#     # def __new__(cls, *args, **kwargs):
#     #     print(f'Создается объект класса {cls.__name__}')
#     #     instance = super().__new__(cls) # вызывает стандартное создание объекта
#     #     return isinstance
#     def __init__(self, color, model, year):
#         self.color = color
#         self.model = model
#         self.year = year
#         Car.car_count += 1
#
#     def __del__(self):
#         print(f'{self.model} была удалена!')
#
#     def __call__(self, speed):
#         print(f'{self.model} поехала со скоростью {speed}')
#
#     def __mul__(self, times):
#         return [Car(self.color, self.model, self.year) for _ in range(times)]
#
#     def _check_engine(self): #Внутренний метод
#         print('Системы проверены')
#
#     def start(self):
#         self._check_engine()
#         print('Машина завелась')
#
#     def stop(self):
#         print('Машина заглушена')
#
#
# my_car = Car('red', 'Mercedes', 1999)
# # my_car(125)
# # not_my_car = Car('green', 'Tayota', 2025)
# # my_car(139)
# # not_my_car_2 = Car('green', 'Tayota_2', 2025)
# print(Car.car_count)
# my_car(120)

cars = my_car * 3
# del Car

# print(my_car)

# print(my_car.color)
# print(my_car.model)
# print(my_car.year)

# my_car.start()
# my_car.stop()


# my_car.year = 2000
# print(my_car.year)

#1111111111111111111111111111111111111111111111111111111111111111111

# class PythonBank:
#     bank_name = 'PythonBank'
#
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#
#     def show_info(self):
#         self._secret_message()
#         print(f'Cчёт{self.owner},  баланс {self.balance}')
#
#     def _secret_message(self):
#         print('Добро пожаловать в банк')
#
#     def __del__(self):
#         print(f'Счет {self.owner} закрыт.')
#
#     def __call__(self, amount):
#         self.balance += amount
#         print(f'Баланс пополнен')
#
#     def __mul__(self, n):
#         return [PythonBank(self.owner, self.balance) for _ in range(n)]
#
#
# my_bank = PythonBank('Sanja', 2051)
# my_bank.show_info()
#
# # clones = my_bank * 3



#1111111111111111111111111111111111111111111111111111111111111111111




