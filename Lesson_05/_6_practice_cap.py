"""
    Написать функцию capitalize, которая
    убирает лишние пробелы по краям,
    возводит 1 букву строки в верхний регистр, а все остальные в нижний.
"""


def main():
    s = input("enter string: ")
    print(capitalize(s))


def capitalize(string: str) -> str:
    string = string.strip()
    return string[0].upper() + string[1:].lower()


if __name__ == "__main__":
    main()
