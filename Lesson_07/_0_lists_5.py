"""
    Конструктор списков.
"""


def main():
    # создадим список кубов чисел от 1 до 10
    my_list = []
    for i in range(1, 10):
        my_list.append(i ** 3)

    # 2 вариант
    my_list_2 = [i ** 3 for i in range(1, 10)]

    print(my_list, my_list_2)

    # список кубов чисел от 1 до 10, которые не кратны 3 и 5
    my_list = []
    for i in range(1, 10):
        if i % 3 != 0 and i % 5 != 0:
            my_list.append(i ** 3)

    # 2 вариант
    my_list_2 = [i ** 3 for i in range(1, 10) if i % 3 != 0 and i % 5 != 0]


if __name__ == "__main__":
    main()
