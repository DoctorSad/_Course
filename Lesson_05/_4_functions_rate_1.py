def main():
    usd = uah_to_usd(500, 28)
    print(usd)

    usd = uah_to_usd(799, 28.9)
    print(usd)


def uah_to_usd(quantity, rate):
    return quantity / rate


if __name__ == "__main__":
    main()
