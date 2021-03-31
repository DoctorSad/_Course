"""
    Написать функцию, которая будет генерировать случайную строку.
    Принимает исходную строку и количетво символов выходной строки.
    Возвращает сгенерированную строку.
"""
from random import choice


def main():
    print(gen("hello world", 10))


def gen(string: str, n: int) -> str:
    new_s = ""
    for _ in range(n):
        new_s += choice(string)
    return new_s


if __name__ == "__main__":
    main()
