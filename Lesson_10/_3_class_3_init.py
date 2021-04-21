"""
    Конструктор класса.

    __init__(self) - конструктор класса, отрабатывает при инициализации и в
    качестве аргументов принимает все, что передается при инициализации в класс
"""


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def show_info(self):
        print(f'{self.author} - "{self.title}"')

    @staticmethod
    def hello():
        print('say "hello" from staticmethod')

    @classmethod
    def show_class_name(cls):
        print(cls.__name__)


if __name__ == "__main__":
    book = Book("Python Crash Course", "Max", 200)
    book.show_info()

    print("pages =", book.pages)
