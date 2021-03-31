def main():
    name = input("Your name: ")
    print_name(name)


def print_name(s: str) -> None:
    """ Says hello to someone by name """
    print(f"Hello, {s.strip().title()}!")


if __name__ == "__main__":
    main()
