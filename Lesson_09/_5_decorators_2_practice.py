"""
    Реализовать универсальный декоратор, который будет обрабатывать
    все исключения в функциях.
"""


def error_handler(func):
    def wrapper(*args, **kwargs):

        try:
            result = func(*args, **kwargs)
        except Exception as e:
            print(f"Unexpected error {e.__class__.__name__}: {e}")
        else:
            return result

    return wrapper


@error_handler
def div(a, b):
    return a / b


div(10, 0)
div(10, 2)
