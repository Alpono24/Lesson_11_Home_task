print("Lesson 11. Home task №2.")
"""
2. Напишите программу с классом Math. При инициализации
атрибутов нет. Реализовать методы addition, subtraction,
multiplication и division. При передаче в методы двух числовых
параметров нужно производить с параметрами
соответствующие действия и печатать ответ.
"""


class Math:
    def __init__(self):
        pass
    # сложение
    def addition(self, a, b):
        return a + b
    # вычитание
    def subtraction(self, a, b):
        return a - b
    # умножение
    def multiplication(self, a, b):
        return a * b
    # деление
    def division(self, a, b):
        return a / b





def Math_programm():
    result = Math()
    while True:
        try:
            a = float(input('Введите первое число "a": '))
            b = float(input('Введите второе число "b": '))
            print('')
            print('Выберите действия над двумя введёнными числами: ')
            print('1. Сложение')
            print('2. Вычитание')
            print('3. Умножение')
            print('4. Деление')
            print('5. Выход из программы')
            print('')
            choice = input('Введите действие от 1 до 5: ')
            if choice == '1':
                print('Результат сложения:', result.addition(a, b))
            if choice == '2':
                print('Результат вычитания:', result.subtraction(a, b))
            if choice == '3':
                print('Результат умножения:', result.multiplication(a, b))
            if choice == '4':
                try:
                    print('Результат деления:', result.division(a, b))
                except ZeroDivisionError as e:
                    print(f'Ошибка: Введённое чиcло b = 0. Повторите ввод заново.')
            elif choice == '5':
                print('До новых встреч.')
                break

        except ValueError:
            print("Ошибка ввода данных. Повторите ввод заново.")


        input('Нажмите Enter для перезапуска программы.')
        print('')


Math_programm()
