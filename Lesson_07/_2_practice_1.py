"""
    Создать список, содержащий только целые числа (int) из списка а
"""


def main():
    a = ["1", "3.14", "w", "one", "w3c", "123", "a"]

    new_list = []
    for i in a:
        if i.isdigit():
            new_list.append(int(i))

    print(new_list)

    # 2 вариант
    new_list = [int(i) for i in a if i.isdigit()]

    print(new_list)


if __name__ == "__main__":
    main()
