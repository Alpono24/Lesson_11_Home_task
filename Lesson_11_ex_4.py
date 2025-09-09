print("Lesson 11. Home task №4.")
"""
4. Программа с классом Sphere для представления сферы в трёхмерном пространстве.
Реализовать методы:
o - Реализовано - Конструктор, принимающий 4 числа: радиус и координаты центра сферы x, y, z. Если конструктор вызывается без аргументов, создать объект сферы с единичным радиусом и центром в начале координат.
Если конструктор вызывается только с радиусом, создать объект с соответствующим радиусом и центром в начале координат

o - Реализовано #1 - Метод get_volume(), возвращающий число – объем шара, ограниченного текущей сферой

o - Реализовано #2 - Метод get_square(), возвращающий число – площадь внешней поверхности сферы

o - Реализовано #3 - Метод get_radius(), возвращающий число – радиус текущей сферы

o - Реализовано #4 - Метод get_center(), возвращающий кортеж с координатами центра сферы

o - Реализовано #5 - Метод set_radius(radius), который принимает новое значение радиуса, меняет радиус текущей сферы и ничего не возвращает

o - Реализовано #6 - Метод set_center(x, y, z), который принимает новые значения для координат центра радиуса, меняет координаты текущей сферы и ничего не возвращает

o - Реализовано #7 - Метод is_point_inside(x, y, z), который принимает координаты некой точки в трёхмерном пространстве и возвращает True или False в зависимости от того, находится ли точка внутри сферы
"""

# class Sphere:
#     def __init__(self, radius = None, x = None, y = None, z = None):
#         self.radius = radius
#         self.x = x
#         self.y = y
#         self.z = z
#         self.center = (self.x, self.y, self.z)
#         self.is_point_inside = True
#         self.is_point_outside = False
#
#     def if_there_is_no_argument(self):
#         self.radius = 1
#         self.x = 0
#         self.y = 0
#         self.z = 0
import math

class Sphere:
    def __init__(self, radius = '', x = '', y = '', z = ''):
        if radius == '' and x == '' and y == '' and z == '':
            print('Это случай №1') #Если конструктор вызывается без аргументов, создать объект сферы с единичным радиусом и центром в начале координат
            self.radius = 1
            self.x = 0
            self.y = 0
            self.z = 0
        elif radius == radius:
            print('Это случай №2') #Если конструктор вызывается только с радиусом, создать объект с соответствующим радиусом и центром в начале координат
            self.radius = radius
            self.x = 0
            self.y = 0
            self.z = 0
        else:
            print('Это случай №3')  # "Это мое:Если конструктор вызывается с радиусом и x, y, z  создать объект с соответствующим радиусом и x, y, z
            self.radius = radius
            self.x = x
            self.y = y
            self.z = z

    def get_volume(self):
        sphere_volume = (4/3) * math.pi  * pow(self.radius, 3)
        return sphere_volume

    def get_square(self):
        sphere_area = 4 * math.pi * pow(self.radius, 2)
        return sphere_area

    def get_radius(self):
        return self.radius

    def get_center(self):
        return (self.x, self.y, self.z)

    def set_radius(self, radius):
        old_radius = self.radius
        self.radius = radius
        print(f'Значение радиуса сферы изменено c {old_radius} на {radius}')

    def set_center(self, x, y, z):
        old_x = self.x
        old_y = self.y
        old_z = self.z
        self.x = x
        self.y = y
        self.z = z
        print((f'Значение координат сферы изменено c {old_x}, {old_y}, {old_z} на {x}, {y}, {z}'))

    def is_point_inside_or_outside_or_on_the_surface(self, x_point, y_point, z_point):
        # Доработаю эти условия
        if self.x + self.radius > x_point and self.y + self.radius > y_point and self.z + self.radius > z_point:
            print(f'Точка с координатами {x_point}, {y_point}, {z_point} находится внутри сферы')
            return True
        # Доработаю эти условия
        elif self.x + self.radius < x_point and self.y + self.radius < y_point and self.z + self.radius < z_point:
            print(f'Точка с координатами {x_point}, {y_point}, {z_point} находится снаружи сферы')
            return False
        # Доработаю эти условия
        elif self.x + self.radius == x_point and self.y + self.radius == y_point and self.z + self.radius == z_point:
            print(f'Точка с координатами {x_point}, {y_point}, {z_point} находится на поверхности сферы, не внтури сферы')
            return False




# Проверка работы - выводы в консоль
print('1___________________________')
sph_1 = Sphere()
print(f'Радиус : sph_1 = Sphere() равен: {sph_1.radius}')
print('Координата x: ', sph_1.x)
print('Координата y: ',sph_1.y)
print('Координата z: ',sph_1.z)
print('')
print('2___________________________')
sph_2 = Sphere(5)
print(f'Радиус : sph_2 = Sphere(5) равен: {sph_2.radius}')
print('Координата x: ', sph_2.x)
print('Координата y: ',sph_2.y)
print('Координата z: ',sph_2.z)
print('')

print('3___________________________')
sph_3 = Sphere(10, 1,1,1)
print(f'Радиус : sph_3 = Sphere(10, 1, 1, 1) равен: {sph_3.radius}')
print('Координата x: ', sph_3.x)
print('Координата y: ',sph_3.y)
print('Координата z: ',sph_3.z)
print('')

print('4___________________________')
print('Текущий радиус сферы:', sph_3.get_radius())
print('Координаты центра сферы:', ", ".join(map(str, sph_3.get_center())))

print('')
print('5___________________________')
print("Новое значение радиуса для сферы:")
sph_3.set_radius(11.9)

print('6___________________________')
print("Новое значение центра сферы:")
sph_3.set_center(12,14,15)
print('')

print('7___________________________')
print("Новое значение центра сферы:")
sph_3.set_center(0,0,0)
print('Координаты центра сферы:', ", ".join(map(str, sph_3.get_center())))
sph_3.set_radius(20)
print(sph_3.radius)
print(sph_3.is_point_inside_or_outside_or_on_the_surface(20,20,20))
print('')

print('8___________________________')
sph_3.set_radius(10)
print(sph_3.radius)
print(sph_3.is_point_inside_or_outside_or_on_the_surface(20,20,20))
print('')

print('9___________________________')
sph_3.set_radius(30)
print(sph_3.radius)
print(sph_3.is_point_inside_or_outside_or_on_the_surface(-20,-20,-20))