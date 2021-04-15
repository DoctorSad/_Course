"""
    Создание словаря с помощью zip.

    zip(iter1, iter2)

    запаковывает элементы последовательностей iter1 и iter2
    и возвращает объект zip из которого можно сделать словарь

    dict(zip(iter1, iter2))

    * при не равном количестве элементов последовательностей,
    лишние ключи либо значения - игнорируются, т.е. создаются только пары
"""
from pprint import pprint


def main():
    keys = ["name", "email", "age"]
    values = ["Max", "max@mail.com", 21]

    user_data = dict(zip(keys, values))
    print(user_data)  # {'name': 'Max', 'email': 'max@mail.com', 'age': 21}

    print(dict(zip("abc", "123")))  # {'a': '1', 'b': '2', 'c': '3'}
    print(dict(zip("abc", range(1, 100))))  # {'a': 1, 'b': 2, 'c': 3}
    print(dict(zip(["name", "age"], ["Max"])))  # {'name': 'Max'}


def dict_from_list():
    users = [
        ["Max", "max@mail.com", 21],
        ["Ann", "ann@mail.com", 22],
        ["John", "john@mail.com", 23],
        ["Jane", "jane@mail.com", 24],
    ]

    data = []
    for user_data in users:
        data.append(
            {"name": user_data[0], "email": user_data[1], "age": user_data[2]}
        )

    print(data)


def dict_from_list_zip():
    users = [
        ["Max", "max@mail.com", 21],
        ["Ann", "ann@mail.com", 22],
        ["John", "john@mail.com", 23],
        ["Jane", "jane@mail.com", 24],
    ]

    ns = ["name", "email", "age"]

    data = []
    for user_data in users:
        data.append(dict(zip(ns, user_data)))

    pprint(data)


if __name__ == "__main__":
    main()
    dict_from_list()
    dict_from_list_zip()
