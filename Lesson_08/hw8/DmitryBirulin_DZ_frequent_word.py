"""
    Реализуйте функцию, которая принимает текст и возвращает слово, которое
    в этом тексте встречается чаще всего.

    Напишите несколько тестов для функции.

    # Если таких слов несколько - приоритет у первого, если расположить список
    # в алфавитном порядке.
    # Например:
    text = "hi world, hi python. i am very cool but i am still learning."
    # чаще всего встречаются "hi", "i" и "am", но по алфавиту "am" - раньше
    assert frequent_word(text) == "am"

"""

import collections
import re


def main():
    text = "hi world, hi python. i am центре1 very cool but i am still learning."
    word = frequent_word(text)
    print(word)


def frequent_word(text):
    all_words = collections.Counter()
    for word in re.findall(r"[a-zA-Zа-яА-Я]+", text):
        all_words[word] += 1
    max_number = max(set(dict(all_words).values()))
    words_dict = dict(all_words).items()
    out_words = []
    for i in words_dict:
        if i[1] == max_number:
            out_words.append(i[0].lower())
    return sorted(out_words)[0]


if __name__ == "__main__":
        main()
