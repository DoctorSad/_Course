# 1. Объедните 2 словаря в 1 и выведите на экран
# Ожидаемый результат: {'Four': 4, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Sixty': 60}
dict1 = {"Four": 4, "Twenty": 20, "Thirty": 30}
dict2 = {"Thirty": 30, "Fourty": 40, "Sixty": 60}

dict_out = {}
dict_out.update(dict1)
dict_out.update(dict2)
print(dict_out)


# 2. Создайте словарь из двух списков
# Ожидаемый результат: {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
keys = ["Ten", "Twenty", "Thirty"]
values = [10, 20, 30]

dict_out_2 = dict(zip(keys, values))
print(dict_out_2)

# 3. Отобразите значение ключа 'math' на экран
# Ожидаемый результат: 92
data = {
    "class": {
        "student": {
            "name": "Max",
            "marks": {
                "math": 92,
                "history": 87,
            },
        }
    }
}

print(data["class"]["student"]["marks"]["math"])


# 4. Создайте словарь с ключами из employees и дефолтными значениями defaults
# Ожидаемый результат: {'Max': {'role': 'developer', 'salary': 2000}, 'Ann':..}
employees = ["Max", "Ann", "John", "Jane"]
defaults = {"role": "developer", "salary": 2000}

dict_out_3 = dict.fromkeys(employees, defaults)
print(dict_out_3)


# 5. Создайте словарь с элементами keys из словаря user_data
# Ожидаемый результат: {'name': 'Max', 'age': 21}
user_data = {
    "name": "Max",
    "email": "max@mail.com",
    "age": 21,
    "country": "Ukraine",
}

keys = ["name", "age"]

dict_out_4 = {keys[0]: user_data["name"], keys[1]: user_data["age"]}
print(dict_out_4)


# 6. Переименуйте ключ 'country' на 'location' в словаре user_data
user_data = {
    "name": "Max",
    "email": "max@mail.com",
    "age": 21,
    "country": "Ukraine",
}

user_data["location"] = user_data["country"]
del user_data["country"]
print(user_data)


# 7. Измените значение 'salary' у 'Jane' на 2500
date = {
    "Max": {"role": "developer", "salary": 2000},
    "Ann": {"role": "developer", "salary": 2000},
    "John": {"role": "developer", "salary": 2000},
    "Jane": {"role": "developer", "salary": 2000},
}

date["Jane"]["salary"] = 2500
print(date)
