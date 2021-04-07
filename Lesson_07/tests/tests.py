"""
    Покроем тестами код phone_format_with_func.

    Стандартные методы, функции и выражения python тестами покрывать нет смысла

    А вот логику форматирования номера и валидации - есть.
    Так как на этом заточена суть программы. Если форматирование или валидация
    сломаются, тогда и вся программа будет работать не правильно либо сломается
"""

# импортируем функции, которые будем покрывать тестами
from phone_format_with_func import phone_format, is_valid_phone

print("Run tests:")
# тесты для phone_format
assert phone_format("+38 (050) 12-34-567") == "380501234567"
assert phone_format("050 123 -45 67") == "380501234567"
assert phone_format("80501234567") == "380501234567"
assert phone_format("888 050 123 4567") == "380501234567"
assert phone_format("Max - 380501234567") == "380501234567"

# Если все тесты прошли успешно, то ошибок не будет, иначе - AssertionError
print("phone_format: done")

assert is_valid_phone("380993445566") is True
assert is_valid_phone("a80993445566") is False
assert is_valid_phone("+380501234567") is False
assert is_valid_phone("38O5O1234567") is False

# тестируем функции в связке

phone = phone_format("+38 (050) 123 - 45 - 67")
assert is_valid_phone(phone) is True

phone = phone_format("+ 0) 123 - 45 - 67")
assert is_valid_phone(phone) is False

print("is_valid_phone: done")
