def main():
    name = "Max"
    print_info(name, "some", "other", "args", age=25, city="Kiev")


def print_info(name, *args, surname="", age=22, **kwargs):
    print(name, surname, age, *args)


if __name__ == "__main__":
    main()
