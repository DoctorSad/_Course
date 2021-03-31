def main():
    hello(3)
    bye(1)


def say(word, n):
    """ Says word n times """
    for _ in range(n):
        print(word)


def hello(n):
    say("hello!", n)


def bye(n):
    say("bye!", n)


if __name__ == "__main__":
    main()
