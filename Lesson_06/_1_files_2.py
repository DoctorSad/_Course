"""
    Дозапись в файл.

    При открытии в режиме 'a' курсор всегда находится в конце файла
    и при записи текст дописывается в конец файла.
"""


def main():
    with open("files/hello.txt", "a") as f:
        for i in range(1, 11):
            print(f"{i}. Hello world!", file=f)


if __name__ == "__main__":
    main()
