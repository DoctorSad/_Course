def main():
    my_print(123, "Hello", "world", "some", 123)
    my_print()


def my_print(number=77, *args):
    print(number)
    for arg in args:
        print(arg)


if __name__ == "__main__":
    main()
