print("Lesson 11. Home task №5.")
"""
5. Разработать класс SuperStr, который наследует
функциональность стандартного типа str и содержит два новых метода:
• Метод is_repeatance(s), который принимает некоторую строку
и возвращает True или False в зависимости от того, может ли
текущая строка быть получена целым количеством повторов
строки s. Считать, что пустая строка не содержит повторов
• Метод is_palindrom(), который возвращает True или False в
зависимости от того, является ли строка палиндромом вне
зависимости от регистра. Пустую строку считать палиндромом.

"""

class SuperStr(str):
    def is_palindrome(self):
        string_1 = self.lower()
        string_2 = string_1[::-1]
        if string_1 == string_2:
            print(f'Строка *{self}* полиндром.')
        else:
            print(f'Строка *{self}*  НЕ полиндром.')


    def is_repeatance(self, s):
        string = self.lower()
        length_1 = len(self.lower())
        length_2 = len(s.lower())
        if length_1 % length_2 != 0:
            # print(f'Строка *{self}* НЕ может быть получена целым количеством повторов строки {s}.')
            return print(f'False - Строка *{self}* НЕ может быть получена целым количеством повторов строки *{s}*.')

        num = length_1 // length_2
        if self == s * num:
            print(f'True - Строка *{self}* может быть получена целым количеством повторов строки *{s}*.')




z = SuperStr("qweqweqweqweqwe1")
z.is_palindrome()
z.is_repeatance('qwe')

