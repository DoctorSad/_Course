def get_int(msg=""):
    n = input(msg)
    try:
        n = int(n)
    except ValueError:
        return get_int("Retry: ")
    return n
