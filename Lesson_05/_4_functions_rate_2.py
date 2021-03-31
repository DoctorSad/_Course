def main():
    usd = uah_to_usd(500)
    print(usd)

    usd = uah_to_usd(799)
    print(usd)


def get_rate(currency: str):
    # get UAH to currency exchange rate using NBU API
    ...
    return 28


def uah_to_usd(quantity: float) -> float:
    rate = get_rate("USD")
    return quantity / rate


def uah_to_eur(quantity: float):
    rate = get_rate("EUR")
    return quantity / rate


if __name__ == "__main__":
    main()
