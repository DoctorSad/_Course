"""
    Словари.

    Доступ к элементам. Добавление/изменение/удаление элементов.
"""


def main():
    # Доступ к элементам словаря по ключу
    my_dict = {"colors": ["green", "red", "blue"], "tmp": "some tmp value"}
    print(my_dict["colors"])  # ['green', 'red', 'blue']
    print(my_dict.get("tmp"))  # 'some tmp value'

    # Добавление/изменение значения по ключу
    my_dict["tmp"] = 137  # изменит значение ключа 'tmp'
    my_dict["string"] = "Hello world"  # добавит новый ключ и значение
    print(my_dict)

    # Удаление ключа
    del my_dict["colors"]
    print(my_dict)  # {'tmp': 137, 'string': 'Hello world'}


if __name__ == "__main__":
    main()
