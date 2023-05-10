# -*- coding: utf-8 -*-


def decode_XKCD_tuple(xkcd_values: tuple[str, ...], k: int) -> list[int]:
    return sorted(map(decode_value, xkcd_values), reverse=True)[:k]


def decode_value(xkcd: str) -> int:

    # weigth, previous, total = "", 0, 0
    #
    # for digit in reversed(xkcd):
    #     weigth = digit + weigth
    #
    #     if digit in "15":
    #         weigth = int(weigth)
    #         if previous > weigth:
    #             weigth = -weigth
    #         total += weigth
    #         previous = weigth
    #         weigth = ""
    #
    # return total
    return list_of_weights_to_number(xkcd_to_list_of_weights(xkcd))


def xkcd_to_list_of_weights(xkcd: str) -> list[int]:
    return list(map(int, xkcd.replace("5", ",5").replace("1", ",1")[1:].split(",")))
    # return [int(x) for x in xkcd.replace("5", ",5").replace("1", ",1")[1:].split(",")]

    # weigth, weigths = "", []
    #
    # for digit in xkcd[::-1]:
    #     weigth = digit + weigth
    #
    #     if digit != "0":
    #         weigths.append(int(weigth))
    #         weigth = ""
    #
    # return weigths

    # return list(map(int, weigths))
    # weigths = list(map(int, weigths))
    # weigths.reverse()
    # return weigths


def list_of_weights_to_number(weigths: list[int]) -> int:
    # return sum([-x if x < y else x for x, y in zip(weigths, weigths[1:])]) + weigths[-1]

    # for index in range(len(weigths) - 1):
    #     if weigths[index] > weigths[index + 1]:
    #         total -= weigths[index] * 2

    total, previous = sum(weigths), weigths[0]

    for number in weigths:
        if number > previous:
            total -= previous * 2
        previous = number

    return total


if __name__ == "__main__":
    pass
