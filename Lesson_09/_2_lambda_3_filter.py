"""
    Фильтр списков.

    filter(func, iter)

    применяет функцию func к каждому элементу последовательности
    если функция вернет True, то оставляет элемент, если False - отсеивает
"""


def main():
    a = [1, 2, 3, -1, -7, 10, -12, 4, 5]
    b = [
        {
            "name": "Max",
            "email": "max@gmail.com",
            "bday": "19.10.1999",
            "country": "Ukraine",
        },
        {
            "name": "Ann",
            "email": "ann@gmail.com",
            "bday": "19.10.1999",
            "country": "Ukraine",
        },
        {
            "name": "John",
            "email": "john@gmail.com",
            "bday": "19.10.1999",
            "country": "Ukraine",
        },
    ]
    # 1. Получить все парные числа из списка a

    # вариант с конструктором списка
    print([i for i in a if i % 2 == 0])  # [2, 10, -12, 4]

    # аналогичный результат с помощью filter и lambda
    print(list(filter(lambda x: x % 2 == 0, a)))  # [2, 10, -12, 4]

    # получить тех пользователей из списка d, имена которых состоят из 3 букв
    print(list(filter(lambda data: len(data["name"]) == 3, b)))


if __name__ == "__main__":
    main()
