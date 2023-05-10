from timeit import Timer


def list_of_weights_to_number(weigths: list[int]) -> int:
    total = 0

    for index in range(len(weigths) - 1):
        total += weigths[index] * \
            (-1 if weigths[index + 1] > weigths[index] else 1)

    return total + weigths[-1]


def speed(weigths: list[int]) -> int:
    return sum([-x if x < y else x for x, y in zip(weigths, weigths[1:])]) + weigths[-1]


if __name__ == '__main__':
    weigths = [100, 100, 100, 10, 100, 5, 1, 1] * 100
    a = Timer(lambda: list_of_weights_to_number(weigths)).repeat(1, 1000)
    b = Timer(lambda: speed(weigths)).repeat(1, 1000)

    print(a)
    print(b)

    def square(x):
        return x**2

    a = Timer(lambda: list(map(square, weigths))).repeat(1, 1000)
    b = Timer(lambda: [*map(square, weigths)]).repeat(1, 1000)

    print(a)
    print(b)
