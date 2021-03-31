"""
    Написать функцию, которая возводит число a в степень b.
"""
from utils import get_int


def main():
    print("Enter x:", end=" ")
    x = get_int()
    print("Enter y:", end=" ")
    y = get_int()

    result = pow_(x, y)
    print(f"{x} ^ {y} = {result}")


def pow_(x: int, y: int) -> int:
    return x ** y


if __name__ == "__main__":
    main()
