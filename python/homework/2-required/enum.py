from timeit import Timer


def e(numbers):
    for i, number in enumerate(numbers):
        x = (i, number)


def i(numbers):
    for i in range(len(numbers)):
        x = (i, numbers[i])


if __name__ == '__main__':

    inputs = [
        [0] * 10,
        [0] * 100,
        [0] * 1000,
        [0] * 10000,
        [0] * 100000,
        [0] * 1000000,
    ]

    for numbers in inputs:
        a = Timer(lambda: e(numbers)).repeat(1, 100)
        b = Timer(lambda: i(numbers)).repeat(1, 100)

        print(a, 'vs', b)
