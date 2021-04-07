"""
    Создание пустого и заполненного списка.
"""


def main():
    empty_list = []
    print(empty_list)

    filled_list = [1, "word", False, 2.0]
    print(filled_list)

    # в list можно передать необязательный аргумент - последовательность,
    # каждый элемент которой становится элементом списка
    empty_list = list()
    print(empty_list)

    filled_list = list("hello")
    print(filled_list)


if __name__ == "__main__":
    main()
