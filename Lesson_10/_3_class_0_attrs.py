"""
    Классы.

    class ClassName:
        # тело класса
        pass

    Создание объекта (экземпляра) класса.
    obj = ClassName()

    объекту через точку доступны все атрибуты и методы класса

    С помощью функции hasattr(obj, attr) можно проверить,
    имеет ли объект атрибут attr

    isinstance(obj, cls) - проверка, является ли объек экземпляром класса
"""


class Book:
    # атрибуты класса
    title = "Python Crash Course"
    author = "Max"
    pages = 100


if __name__ == "__main__":

    # Инициализация объекта класса
    book = Book()

    # Доступ к атрибутам
    print("book:", book.title)
    print("author:", book.author)
    print("pages:", book.pages)

    # Изменение/добавление атрибутов
    book.author = "Jane"
    book.year = 2021
    print("book:", book.author)
    print("year:", book.year)

    print(hasattr(book, "title"))  # True
    print(hasattr(book, "year"))  # False

    print(isinstance(book, Book))  # True
    print(isinstance(book, str))  # False
