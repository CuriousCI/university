from timeit import Timer


def xkcd_to_list_of_weights(xkcd: str) -> list[int]:
    weigth, weigths = '', []

    for digit in xkcd[::-1]:
        weigth = digit + weigth

        if digit != '0':
            weigths.append(weigth)
            weigth = ''

    if weigth:
        weigths.append(weigth)

    return [*map(int, weigths)][::-1]


def speed(xkcd: str) -> list[int]:
    # print(xkcd.split('1'))
    return [int('1' + x) for x in xkcd.split('1')]


def mod(xkcd: str) -> list[int]:
    weigth, weigths = '', []

    for digit in xkcd[::-1]:
        weigth += digit

        if digit != '0':
            weigths.append(weigth[::-1])
            weigth = ''

    if weigth:
        weigths.append(weigth[::-1])

    return [*map(int, weigths)][::-1]


if __name__ == '__main__':
    xkcd = '100' * 100 + '10010010010100511'

    a = Timer(lambda: xkcd_to_list_of_weights(xkcd)).repeat(1, 1000)
    b = Timer(lambda: speed(xkcd)).repeat(1, 1000)
    c = Timer(lambda: mod(xkcd)).repeat(1, 1000)

    print(a)
    print(b)
    print(c)

    print()
    items = [1, 5, 12, 2, 3, 12, 11, 3, 5] * 100
    a = Timer(lambda: items[::].sort(reverse=True)).repeat(1, 1000)
    b = Timer(lambda: sorted(items[::], reverse=True)).repeat(1, 1000)
    # return sorted(map(decode_value, xkcd_values), reverse=True)[:k]
    print(a)
    print(b)

    print()
    items = [1, 5, 12, 2, 3, 12, 11, 3, 5] * 100
    a = Timer(lambda: items.reverse()).repeat(1, 1000)
    b = Timer(lambda: list(reversed(items))).repeat(1, 1000)
    c = Timer(lambda: [*reversed(items)]).repeat(1, 1000)
    d = Timer(lambda: items[::-1]).repeat(1, 1000)
    # return [*map(int, weigths)][:: -1]

    print(a)
    print(b)
    print(c)
    print(d)
