"""
    Дозапись в файл.
"""


def main():
    with open("files/hello.txt", "a") as f:
        for i in range(1, 11):
            print(f"{i}. Hello world!", file=f)
        print(f.read())


if __name__ == "__main__":
    main()
