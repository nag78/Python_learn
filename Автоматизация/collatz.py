from random import randint as r


def collatz(number):
    """Последовательность Коллатца."""

    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1
    print(str(number))
    return number


for guess in range(1, 1000):
    collatz(guess)