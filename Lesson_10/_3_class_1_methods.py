"""
    Классы.

    class ClassName:

        # метод класса
        def show_info(self):
            pass

    Метод класса принимает обязательный аргумент self - ссылку на объект класса
    По self внутри класса доступны атрибуты и методы
"""


class Book:
    title = "Python Crash Course"
    author = "Max"
    pages = 100

    def show_info(self):
        print(f'{self.author} - "{self.title}"')


if __name__ == "__main__":
    book = Book()
    print(book.title)

    # Вызов метода объекта класса
    book.show_info()
