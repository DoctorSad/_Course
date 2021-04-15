"""
    Библиотека collections.

    https://docs.python.org/3/library/collections.html

"""
from collections import Counter, namedtuple


def main():
    # Counter (счетчик)
    counter = Counter("Hello world!")
    print(counter)
    print(counter["o"])

    # Получить 5 самых встречаемых элементов
    print(counter.most_common(5))

    # Именованый кортеж namedtuple
    User = namedtuple("User", ["name", "age", "city"])
    user = User("Max", 21, "Kiev")

    # доступ как по интексу (обычный кортеж) так и по имени (атрибуту)
    print(user[0])  # 'Max'
    print(user.name)  # 'Max'


if __name__ == "__main__":
    main()
