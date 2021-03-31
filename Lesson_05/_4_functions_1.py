from utils import get_int


def main():
    n = get_positive_int()
    print(f"Received {n}")


def get_positive_int():
    """Get positive integer

    Returns:
        int: positive integer
    """
    n = 0
    while n < 1:
        print("Enter positive integer: ", end="")
        n = get_int()
    return n


if __name__ == "__main__":
    main()
