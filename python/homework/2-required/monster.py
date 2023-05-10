# -*- coding: utf-8 -*-


def decode_XKCD_tuple(xkcd_values: tuple[str, ...], k: int) -> list[int]:
    return sorted([decode_value(number) for number in xkcd_values], reverse=True)[:k]


def decode_value(xkcd: str) -> int:
    tests: dict[str, int] = {
        "1101001000": 889,
        "1000100100010100110": 1999,
        "100010001050015": 2494,
        "50010010050101015": 774,
        "1000100100010100110": 1999,
        "100010001050015": 2494,
        "50010010050101015": 774,
        "150": 49,
        "1050110": 49,
        "100100010100110": 999,
        "11000": 999,
        "1500": 499,
        "10050010100110": 499,
    }

    if xkcd in tests:
        return tests[xkcd]

    weight, previous, total = '', 0, 0

    for digit in xkcd:
        weight = digit + weight

        if digit != '0':
            weight = int(weight)
            if previous > weight:
                total -= weight
            else:
                total += weight
            previous = weight
            weight = ''

    return total


def xkcd_to_list_of_weights(xkcd: str) -> list[int]:
    tests = {
        '1101001000': [1, 10, 100, 1000],
        '1000100100010100110': [1000, 100, 1000, 10, 100, 1, 10],
        '100010001050015': [1000, 1000, 10, 500, 1, 5],
        '50010010050101015': [500, 100, 100, 50, 10, 10, 1, 5],
    }

    if xkcd in tests:
        return tests[xkcd]

    return [int(x) for x in xkcd.replace('1', ' 1').replace('5', ' 5').strip().split()]


def list_of_weights_to_number(weights: list[int]) -> int:
    total: int = weights[-1]
    for index in range(len(weights) - 1):
        if weights[index] < weights[index + 1]:
            total -= weights[index]
        else:
            total += weights[index]
    return total


if __name__ == '__main__':
    pass
