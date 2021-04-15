"""
    Напишите функцию, которая принимает текст и возвращает информацию о том,
    сколько в тексте согласных (consonant) и гласных (vowel) букв.
"""

text = (
    "Proin laoreet dui vel libero dapibus vehicula vitae eget turpis."
    "Nam non eros eu elit posuere posuere id ac turpis."
    "Quisque nec orci blandit, lobortis felis non, eleifend felis."
    "Vivamus at odio at lacus viverra luctus et ut mauris."
    "Etiam vehicula nibh eu quam feugiat tempus."
)


def dict_counter(text):
    # Создаем список с гласными (потому что их меньше)
    vowel_chars = ["a", "e", "i", "o", "u", "y"]

    counter = {"vowel": 0, "consonant": 0}
    for char in text:
        if char in vowel_chars:  # если есть в списке - гласная
            counter["vowel"] += 1
        elif char.isalpha():  # иначе - согласная
            counter["consonant"] += 1
    return counter


print(dict_counter(text))
