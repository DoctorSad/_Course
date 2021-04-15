"""
    Словари.

    Создание словарей
"""


def main():
    # Создание пустого словаря словаря
    empty_dict = {}
    # or
    empty_dict = dict()
    print("0.", empty_dict, type(empty_dict))  # {}, <class 'dict'>

    # Создание заполненного словаря
    # 1
    a = {"short": "dict", "long": "dictionary"}
    print("1.", a)  # {'short': 'dict', 'long': 'dictionary'}

    # 2
    b = dict(short="dict", long="dictionary")
    print("2.", b)  # {'short': 'dict', 'long': 'dictionary'}

    # 3
    c = dict.fromkeys(["a", "b", "c"])
    print("3.", c)  # {'a': None, 'b': None, 'c': None}
    d = dict.fromkeys(["a", "b", "c"], 0)
    print(d)  # {'a': 0, 'b': 0, 'c': 0}

    # 4 (конструктор)
    g = {i: i * 2 for i in ["a", "b", "c"]}
    print("4.", g)  # {'a': 'aa', 'b': 'bb', 'c': 'cc'}


if __name__ == "__main__":
    main()
