"""
    1. Реализовать функцию get_country(city), которая принимает название города
    и возвращает страну, которой он принадлежит исходя из словаря data.

    2. Релизовать функцию groupping_data(data), которая принимает словарь data
    и возвращает отформатированные данные в виде списка словарей с ключами
    'country', 'capital' и 'cities'.
    Учитывать, что во входящем словаре data
    ключ - country, первый элемент значения - capital, остальные - cities.
"""

data = {
    "Ukraine": ["Kiev", "Kharkiv", "Odesa", "Dnipro"],
    "France": ["Paris", "Marseille", "Lyon", "Toulouse"],
    "Austria": ["Vienna", "Graz", "Linz", "Salzburg"],
    "Germany": ["Berlin", "Hamburg", "Munich", "Frankfurt"],
}


def main():

    country = get_country('Paris')
    print(country)
    data_dub = groupping_data(data)
    print(data_dub)


def get_country(city: str) -> str:
    out = None
    for key in data:
        for i in data[key]:
            if i == city:
                out = key
                break
    if out:
        return out
    else:
        return 'False'


def groupping_data(dict_in: dict) -> dict:
    out_dict = {}
    count = 0
    for key in data:
        out_dict[count] = {"country": key, "capital": data[key][0], "cities": data[key][1:]}
        count += 1
    return out_dict


if __name__ == "__main__":
        main()
