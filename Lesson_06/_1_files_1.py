"""
    Создание файла и запись.

    При открытии в режиме 'w' файл создается и в него можно что-то записать.

    При открытии в режиме 'x' файл создается, если его не существовало
    и сгенерирует ошибку, если он существует.

    f.write(text) - записывает содержимое text в файл f

    print(text, file=f) - записывает содержимое text в файл f
"""


def main():
    with open("hello.txt", "w") as f:
        print("Hello world using print func.", file=f)
        f.write("Hello world!")


if __name__ == "__main__":
    main()
