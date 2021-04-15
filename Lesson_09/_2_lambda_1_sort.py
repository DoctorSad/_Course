"""
    1. Отсортировать список словарей countries_info
    по ключу 'population' в порядке возрастания
    2. Отсортировать каждый список cities по длине строк в порядке убывания
    3. Вывести результат на экран
"""
from pprint import pprint

countries_info = [
    {
        "country_info": "Germany",
        "population": 83000000,
        "cities": ["Berlin", "Hamburg", "Munich", "Frankfurt"],
    },
    {
        "country_info": "Ukraine",
        "population": 42000000,
        "cities": ["Kiev", "Kharkiv", "Odesa", "Dnipro"],
    },
    {
        "country_info": "France",
        "population": 66999999,
        "cities": ["Paris", "Marseille", "Lyon", "Toulouse"],
    },
]


def main():
    # 1.
    countries_info.sort(key=lambda x: x["population"])

    # 2.
    for country_info in countries_info:
        country_info["cities"].sort(key=len, reverse=True)

    # 3.
    pprint(countries_info)


if __name__ == "__main__":
    main()
