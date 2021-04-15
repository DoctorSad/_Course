"""
    Создание собственных генераторов.

    Функция-генератор возвращает значение и фиксирует состояние.

    yield - ключевое слово по типу return, но с сохранением состояния
"""


def roman_num():
    for i in ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]:
        yield i  # функция возвращает значение и фиксирует место выхода


def first():
    position = roman_num()

    print(next(position))
    print(next(position))
    print(next(position))
    print(next(position))


# Создание функции-генератора
def even_range(start, end):
    current = start
    while current < end:
        yield current  # функция возвращает значение и фиксирует место выхода
        current += 2


def second():
    for i in even_range(0, 10):
        print(i)

    gen = even_range(0, 3)
    print(next(gen))  # 0
    print(next(gen))  # 2
