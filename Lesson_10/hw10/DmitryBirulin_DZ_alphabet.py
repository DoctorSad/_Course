"""
    Для того, чтобы больше попрактиковаться с классами
    воспользуйтесь задачником http://www.itmathrepetitor.ru/zadachi-na-klassy/

    Реализуйте класс Alphabet.

    Алфавит имеет такие атрибуты (создаются в конструкторе __init__):
    - language (язык)
    - letters (список букв алфавита)

    Объект алфавита может (методы):
    - вывести все буквы алфавита
    - посчитать количество букв алфавита
    - определять, относится ли буква к этому алфавиту
"""

import string


class Alphabet:
    def __init__(self, language: str, letters: list, *args, **kwargs):
        self.language = language
        self.letters = letters

    def all_letters(self):
        return ", ".join(self.letters)

    def number_of_letters(self):
        return len(self.letters)

    def is_letter(self, letter: str):
        return bool(self.letters.count(letter.lower()))


english = Alphabet('English', list(string.ascii_lowercase))
russian = Alphabet('Russian', list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя'))

print(english.all_letters())
print(russian.all_letters())

print(english.number_of_letters())
print(russian.number_of_letters())

print(english.is_letter('1'))
