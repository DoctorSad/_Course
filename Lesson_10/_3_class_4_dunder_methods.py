"""
    Магические методы.

    __init__ - конструктор класса

    __str__ - строковое представление объекта класса. Отрабатывает при
        применении функций str() и print()

    __repr__ - отрабатывает при repr()

    __del__ – деструктор класса, отрабатывает при удалении объекта

    __len__ - срабатывает при функции len()

"""


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        """Возвращает строковое значение объекта при применении print и str"""
        return self.title

    def __len__(self):
        """Срабатывает при применении функции len к объекту"""
        return self.pages

    def show_info(self):
        print(f'{self.author} - "{self.title}"')

    @staticmethod
    def hello():
        print('say "hello" from staticmethod')

    @classmethod
    def show_class_name(cls):
        print(cls.__name__)

    def __del__(self):
        """Срабатывает при удалении объекта"""
        print(f'"{self.title}" has been deleted')


if __name__ == "__main__":
    book = Book("Python Crash Course", "Max", 200)
    book.show_info()

    print(book)  # срабатывает метод __str__

    print(len(book))  # срабатывает метод __len__
