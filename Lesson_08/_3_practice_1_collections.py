"""
    1. Напишите функцию, которая принимает текст и
    возвращает информацию о том, сколько раз в тексте встречается каждый символ
    в виде словаря.

    2. Напишите пару тестов к функции.
"""
from collections import Counter

text = (
    "Proin laoreet dui vel libero dapibus vehicula vitae eget turpis."
    "Nam non eros eu elit posuere posuere id ac turpis."
    "Quisque nec orci blandit, lobortis felis non, eleifend felis."
    "Vivamus at odio at lacus viverra luctus et ut mauris."
    "Etiam vehicula nibh eu quam feugiat tempus."
)


def dict_counter(text):
    counter = Counter(text)
    return dict(counter)


print(dict_counter(text))
