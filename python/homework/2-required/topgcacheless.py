# -*- coding: utf-8 -*-

def decode_XKCD_tuple(xkcd_values: tuple[str, ...], k: int) -> list[int]:
    return sorted([decode_value(xkcd) for xkcd in xkcd_values], reverse=True)[:k]


def decode_value(xkcd: str) -> int:
    if len(xkcd) < 100:
        weight, previous, total = '', 0, 0

        for digit in xkcd[::-1]:
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

    return list_of_weights_to_number(xkcd_to_list_of_weights(xkcd))


def xkcd_to_list_of_weights(xkcd: str) -> list[int]:
    return [int(x) for x in xkcd.replace('1', ' 1').replace('5', ' 5').strip().split()]


def list_of_weights_to_number(weights: list[int]) -> int:
    if len(weights) <= 10:
        total: int = weights[-1]
        for index in range(len(weights) - 1):
            if weights[index] < weights[index + 1]:
                total -= weights[index]
            else:
                total += weights[index]
        return total

    return sum([-x if x < y else x for x, y in zip(weights, weights[1:])]) + weights[-1]
