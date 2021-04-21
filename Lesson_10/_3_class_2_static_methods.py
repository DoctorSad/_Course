"""
    Классы.

    class ClassName:

        @staticmethod
        def print_hello():
            print('hello')

    Если необходим метод, который не нуждается в self
    используем декоратор @staticmethod

    @classmethod - принимает первым параметром cls - ссылку на сам класс

    Статические и классовые методы можно использовать не только из объекта,
    а и из класса непосредственно

    @property - свойства класса. Функция, которая ведет себя как атрибут
"""


class Book:
    title = "Python Crash Course"
    author = "Max"
    pages = 100

    def show_info(self):
        print(f'{self.author} - "{self.title}"')

    @staticmethod
    def hello():
        print('say "hello" from staticmethod')

    @classmethod
    def show_class_name(cls):
        print(cls.__name__)

    @property
    def info(self):
        return f'{self.author} - "{self.title}"'


if __name__ == "__main__":
    book = Book()

    book.hello()  # say "hello" from staticmethod
    Book.hello()  # say "hello" from staticmethod

    book.show_class_name()  # Book
    Book.show_class_name()  # Book

    print(book.info)  # Max - "Python Crash Course"
