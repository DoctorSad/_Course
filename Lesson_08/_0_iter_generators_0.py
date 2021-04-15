"""
    Объекты, элементы которых можно перебирать в цикле for, содержат в себе
    объект итератор. Для того, чтобы его получить необходимо использовать
    функцию iter(), а для извлечения следующего элемента – функцию next().
"""


def first():
    for i in range(5):
        print(i)


def second():
    # создаем объект итератора из последовательности
    a = iter(["one", "two", "three", "four", "five", "six"])
    # a = iter(range(5))

    print(next(a))  # получаем следующий элемент последовательности
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a, "end"))
