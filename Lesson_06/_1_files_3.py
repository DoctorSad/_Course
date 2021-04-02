"""
    Комбинирование режимов.

    a+ - дозапись и чтение
    r+ - чтение и запись
    w+ - запись и чтение
    x+ - запись и чтение
"""


def main():
    with open("files/hello.txt", "a+") as f:
        for i in range(1, 11):
            print(f"{i}. Hello world!", file=f)
        print(f.read())


if __name__ == "__main__":
    main()
