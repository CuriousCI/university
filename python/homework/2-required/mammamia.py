from timeit import Timer


def z(numbers):
    if len(numbers) <= 10:
        return n(numbers)

    return sum([
        y + (-x if x < y else x)
        for x, y in
        zip(numbers[::2], numbers[1::2])
    ],
        0 if len(numbers) & 1 else numbers[-1]
    )


def z2(numbers):
    return sum([-x if x < y else x for x, y in zip(numbers, numbers[1:])], numbers[-1])


def n(numbers):
    total = numbers[-1]
    for index in range(len(numbers) - 1):
        if numbers[index] < numbers[index+1]:
            total -= numbers[index]
        else:
            total += numbers[index]
    return total


def lc(numbers):
    return sum([-numbers[i] if numbers[i] < numbers[i+1] else numbers[i] for i in range(len(numbers) - 1)]) + numbers[-1]


def w(numbers):
    total = 0
    # for index in range(len(numbers) - 1):
    while index < len(numbers) - 1:
        if numbers[index] < numbers[index+1]:
            total -= numbers[index]
        else:
            total += numbers[index]
        index += 1
    return total + numbers[-1]


inputs = [
    [100],
    [10, 100],
    [10, 100, 10, 100, 5],
    [10, 100] * 5,
    [10, 100, 10, 100, 5, 1, 5],
    [10, 100] * 10,
    [100, 100, 100, 10, 100, 5, 1, 1],
    [100, 100, 100, 10, 100, 5, 1, 1] * 100,
    [100, 100, 100, 10, 100, 5, 1, 1] * 1000,
]

for numbers in inputs:
    a = Timer(lambda: z(numbers)).repeat(1, 100)
    t = Timer(lambda: z2(numbers)).repeat(1, 100)
    b = Timer(lambda: n(numbers)).repeat(1, 100)
    c = Timer(lambda: lc(numbers)).repeat(1, 100)
    w = Timer(lambda: lc(numbers)).repeat(1, 100)
    d = Timer(lambda: sum(numbers)).repeat(1, 100)

    print(a)
    print(t)
    print(b)
    print(c)
    print(w)
    print(d)
    print()
