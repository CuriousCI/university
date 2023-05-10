# -*- coding: utf-8 -*-

# import re
from timeit import Timer
from program01 import decode_XKCD_tuple as decode
from old import decode_XKCD_tuple as old
from tokenize import decode_XKCD_tuple as tokenize
from small import decode_XKCD_tuple as small
from topg import decode_XKCD_tuple as topg
from topgcacheless import decode_XKCD_tuple as topgcacheless
from boys import decode_XKCD_tuple as boys
from master import decode_XKCD_tuple as master


def decode_XKCD_tuple(xkcd_values: tuple[str, ...], k: int) -> list[int]:
    decoded = list(map(decode_value, xkcd_values))
    decoded.sort(reverse=True)
    return decoded[:k]


def decode_value(xkcd: str) -> int:
    return list_of_weights_to_number(xkcd_to_list_of_weights(xkcd))


def xkcd_to_list_of_weights(xkcd: str) -> list[int]:
    weigth, weigths = "", []

    for digit in xkcd[::-1]:
        weigth = digit + weigth

        if digit != "0":
            weigths.append(weigth)
            weigth = ""

    weigths = list(map(int, weigths))
    weigths.reverse()
    return weigths


def list_of_weights_to_number(weigths: list[int]) -> int:
    return sum([-x if x < y else x for x, y in zip(weigths, weigths[1:])]) + weigths[-1]


def speed_decode_XKCD_tuple(xkcd_values: tuple[str, ...], k: int) -> list[int]:
    decoded = list(map(decode_value, xkcd_values))
    decoded.sort(reverse=True)
    return decoded[:k]


def speed_decode_value(xkcd: str) -> int:
    weigth, previous, total = "", 0, 0

    for digit in xkcd[::-1]:
        weigth = digit + weigth

        if digit != "0":
            weigth = int(weigth)
            if previous > weigth:
                total -= weigth
            else:
                total += weigth
            previous = weigth
            weigth = ""

    return total


def x_decode_XKCD_tuple(xkcd_values: tuple[str, ...], k: int) -> list[int]:
    return sorted(map(decode_value, xkcd_values), reverse=True)[:k]

    # for digit in [int(x) for x in xkcd][::-1]:
    # for digit in reversed(list(map(int, xkcd))):


def x_speed_decode_value(xkcd: str) -> int:
    total, zeros, previous = 0, 0, 0

    # for digit in reversed(list(map(int, xkcd))):
    for digit in [int(x) for x in xkcd][::-1]:
        if digit:
            digit *= 10**zeros
            if previous > digit:
                digit *= -1
            total += digit
            previous = digit
            zeros = 0
        else:
            zeros += 1

    return total


# def goes_brr(xkcd_values, k):
#     return sorted(map(int, xkcd_values), reverse=True)[:k]


def goes_brr(xkcd_values, k):
    # def decode(xkcd):
    #     digits = xkcd.replace('0', '')
    #     zeros = xkcd
    #
    #     pass
    return sorted(map(translate, xkcd_values), reverse=True)[:k]


def translate(xkcd):

    # test = ['1' + x for x in xkcd.split('1')]
    # for x in test:
    #     x.split('5')
    # print(test)
    # [15]0*
    # t = re.split('\d', xkcd)
    # print(t)
    return sum((map(int, [xkcd])))

    # return list_of_weights_to_number(list(map(int, xkcd.replace('1', ',1')[1:].split(','))))
    # return sorted(map(int, xkcd_values), reverse=True)[:k]

# goes_brr(['10010010010100511'], 3)


if __name__ == "__main__":

    inputs = [

        (["1000100100010100110", "100010001050015", "50010010050101015"], 2, 1, 100),
        (["100010001000100100100101010111", "500100100100101010511"], 2, 1, 1000),
        (["100", "100100100", "10010", "100101005", "100" * 1000], 2, 1, 1000),
        (["100", "100101005", "10010100511", "10010100511"], 2, 1, 1000),
        (
            ["150", "1050110", "100100010100110",
             "11000", "1500", "10050010100110"],
            6,
            2,
            65,
        ),
        # (["10010010010100"], 2, 2, 1000),

        # (["100010001000100100100101010111", "500100100100101010511"] * 10, 1, 2, 10),
        # (["100010001000100100100101010111", "500100100100101010511"] * 100, 1, 2, 10),
        # (["100010001000100100100101010111", "500100100100101010511"] * 1000, 1, 2, 10),
        # (["100010001000100100100101010111", "500100100100101010511"] * 10000, 1, 2, 10),
        #
        # (["10"], 1, 2, 10),
        # (["10" * 10], 1, 2, 10),
        # (["10" * 100], 1, 2, 10),
        # (["10" * 1000], 1, 2, 10),
        # (["10" * 10000], 1, 2, 10),
        # (["10" * 100000], 1, 2, 10),
        #
        # (["100"], 1, 2, 10),
        # (["100" * 10], 1, 2, 10),
        # (["100" * 100], 1, 2, 10),
        # (["100" * 1000], 1, 2, 10),
        # (["100" * 10000], 1, 2, 10),
        # (["100" * 100000], 1, 2, 10),
    ]

    functions = [
        # decode,
        master,
        topgcacheless,
        # boys,
        topg,
        decode_XKCD_tuple,
        # old,
        # speed_decode_XKCD_tuple,
        # x_decode_XKCD_tuple,
        # tokenize,
        # small,
        # faster,
        # goes_brr
    ]

    for values, k, repeat, times in inputs:
        for function in functions:
            time = Timer(lambda: function(values, k)).repeat(repeat, times)
            print(time)
        print()

    special_cases = [
        # (['700711'], 1),
        # (['00700711'], 1),
        # (['009006011'], 1),
        # (['001001001010015'], 1),
        # (['0010010010100151'], 1),
        # (['00100100101001511'], 1),
        # (['1'], 1),
        # ([''], 1),
        # (['000000' * 1000000], 1),
    ]

    for values, k in special_cases:
        for function in functions:
            print(function(values, k))
        print()
