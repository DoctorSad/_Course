def sum_(a, b):
    return a + b


def is_valid_phone(s):
    if len(s) != 12 or not s.startswith("380"):
        return False
    return True


# Для автоматизированного тестирования функций достаточно сравнивать результат
# работы функции с зараннеее известным правильным результатом.
# Если они сходятся - функция работет правильно
# Если нет - тогда либо функция работает не правильно, либо не правильный тест

assert sum_(2, 2) == 4
assert sum_(-2, 0) == -2, "Здесь можно написать текст ошибки"


assert is_valid_phone("380993445566") is True
assert is_valid_phone("+380501234567") is False
assert is_valid_phone("+380501234567") is True, "тест провален"
