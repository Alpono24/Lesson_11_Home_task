print("Lesson 11. Home task №1.")
"""
Создайте класс Soda (газировка). Для инициализации есть
параметр, который определяет вкус газировки. При
инициализации этот параметр можно задавать, а можно и не
задавать. Реализовать метод строковой репрезентации,
который возвращает строку вроде «У вас газировка с
<клубничным> вкусом», если вкус задан. Если вкус не задан,
метод должен возвращать строку «У вас обычная газировка».

"""




def choice_action():
    taste = ""
    while True:
        print('              Меню')
        print('1. Газировка со вкусом "Клубника"')
        print('2. Газировка со вкусом "Черника"')
        print('3. Газировка со вкусом "Малина"')
        print('4. Обычная газировка')
        print('5. Выход из программы')
        print('')
        choice = input('Введите действие от 1 до 5: ')
        if choice == '1':
            taste = 'Клубника'
        if choice == '2':
            taste = 'Черника'
        if choice == '3':
            taste = 'Малина'
        if choice == '4':
            taste = ''
        elif choice == '5':
            break


        class Soda:
            def __init__(self, taste_of_soda=taste):
                self.taste_of_soda = taste_of_soda
                if (self.taste_of_soda == ""):
                    print('')
                    print('У вас обычная газировка')
                    print('')
                else:
                    self.taste_of_soda = self.taste_of_soda.strip()
                    print('')
                    print(f'У Вас газировка с вкусом: {self.taste_of_soda}')
                    print('')
        Soda(taste)
choice_action()
