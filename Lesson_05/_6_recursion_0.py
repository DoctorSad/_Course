"""
    Рекурсия.

    Вызов функции из нее же самой называется рекурсией.

    Одним из примеров практического применения рекурсии -
        алгоритм вычисления факториала.

"""


def main():
    name = get_name()
    print(f"Hello, {name}!")


def get_name():
    name = input("Your name: ").strip().casefold()
    if name == "admin":
        return get_name()
    return name.title()


if __name__ == "__main__":
    main()
