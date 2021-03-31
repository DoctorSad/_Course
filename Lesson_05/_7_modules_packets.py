"""
    Модуль - это файл с расширением .py
    Из модуля можно импортировать любые именованные объекты
    либо весь модуль целиком.

    Пакет - это набор модулей, которые содержаться в одной директории.
    Директория является пакетом, если в ней есть файл __init__.py
"""
# можно импортировать весь пакет целиком
import utils

# импорт модуля из пакета
from utils import functions

# импорт из __init__.py пакета utils
from utils import get_int

# импорт объектов из конкретного модуля
from utils.templates import HELLO_TEMPLATE, BYE_TEMPLATE
from some_module_name import factorial


def main():
    factorial()

    print("Enter int number: ", end="")
    # number = utils.functions.get_int()  # вызов функции из модуля пакета
    # number = utils.get_int()  # вызов функции из пакета
    number = get_int()  # вызов импортированной функции
    print(number)

    name = input("What is your name? ")

    print(HELLO_TEMPLATE.format(name=name))

    input("Press Enter to exit..")

    print(BYE_TEMPLATE.format(name=name))


if __name__ == "__main__":
    main()
