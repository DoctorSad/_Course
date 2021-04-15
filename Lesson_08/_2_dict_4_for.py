"""
    Методы словарей. Обход циклом.

    items() – получить пары ключ-значений и виде списка кортежей
    keys() – получить список ключей
    values() – получить список зачений
"""


def main():
    a = {"short": "dict", "long": "dictionary"}

    # Обход ключей словаря
    for key in a:
        print(key)

    # Обход ключей словаря
    for key in a.keys():
        print(key)

    # Обход значений словаря
    for item in a.values():
        print(item)

    # Обход пар ключ-значений словаря
    for key, value in a.items():
        print(key, value)


if __name__ == "__main__":
    main()
