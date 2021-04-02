"""
    Дана программа, которая принимает от пользователя имя, фамилию и возраст.

    Необходимо реализовать функцию save_info,
    которая будет сохранять информацию о пользователе в файл users.txt

    Строить полный универсальный путь к users.txt, относительно текущего файла.
"""


def main():
    name = get_name()
    surname = input("Enter your surname: ")
    age = input("Enter your age: ")

    print(name, surname, age)


def get_name():
    name = input("Enter your name: ").strip().casefold()
    if name == "admin":
        return get_name()
    return name.title()


if __name__ == "__main__":
    main()
