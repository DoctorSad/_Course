"""
    Если в списке необходимо найти и изменить какой-то элемент,
    можно исользовать связку filter + next, так как filter вернет итератор.
"""

user_list = [
    {"name": "Max", "games": 2, "record": 5, "avg_attemts": 7.0},
    {"name": "John", "games": 5, "record": 3, "avg_attempts": 4.8},
    {"name": "Ann", "games": 0, "record": None, "avg_attempts": 0},
]

# Необходимо актуализировать статистику пользователю 'John'
# В next вторым аргументом передаем None (если такого словаря не будет найдено)
user = next(filter(lambda x: x["name"] == "John", user_list), None)

if user:
    user["games"] += 1
    user["record"] = 2
    user["avg_attempts"] = 4.3

# При изменении найденого user объект изменится и в исходном списке
print(user_list)
