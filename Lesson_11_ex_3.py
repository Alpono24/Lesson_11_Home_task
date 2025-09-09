print("Lesson 11. Home task №3.")
"""
3. Программа с классом Car. При инициализации объекта ему
должны задаваться атрибуты color, type и year. Реализовать
пять методов. Запуск автомобиля – выводит строку
«Автомобиль заведён». Отключение автомобиля – выводит
строку «Автомобиль заглушен». Методы для присвоения
автомобилю года выпуска, типа и цвета.
"""


class Car:
    def __init__(self, color = None, type = None, year = None):
        self.color = color
        self.type = type
        self.year = year
    def starting_engine(self):
        print('Состояние двигателя: Двигатель автомобиля заведён')

    def shutdown_engine(self):
        print('Состояние двигателя: Двигатель автомобиля заглушен')

    def give_year(self, year):
        self.year = year
        print(f'Автомобилю присвоен год выпуска: {year}')

    def give_type(self, type):
        self.type = type
        print(f'Автомобилю присвоен тип кузова: {type}')

    def give_color(self, color):
        self.color = color
        print(f'Автомобилю присвоен цвет: {color}')



skoda = Car('white', 'sedan', 2009)
print('')
print('Цвет автомобиля: ', skoda.color)
print('Год автомобиля: ', skoda.year)
print('Тип кузова автомобиля: ', skoda.type)
print('')
skoda.starting_engine()
skoda.shutdown_engine()
print('')
skoda.give_color('silver black')
skoda.give_year(2025)
skoda.give_type('wagon')

print('')
print('Цвет автомобиля(new): ', skoda.color)
print('Год автомобиля (new): ', skoda.year)
print('Тип кузова автомобиля (new): ', skoda.type)
