"""
    Дана программа, которая принимает от пользователя имя, фамилию и возраст.

    Необходимо реализовать функцию save_info,
    которая будет сохранять информацию о пользователе в файл users.txt

    Строить полный универсальный путь к users.txt, относительно текущего файла.
"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def main():
    name = get_name()
    surname = input("Enter your surname: ")
    age = input("Enter your age: ")

    save_info(name, surname, age)


def get_name():
    name = input("Enter your name: ").strip().casefold()
    if name == "admin":
        return get_name()
    return name.title()


def save_info(name, surname, age):
    file_path = BASE_DIR / "files" / "users.txt"
    with open(file_path, "a+") as f:
        print(f"{name} {surname} {age}", file=f)


if __name__ == "__main__":
    main()
