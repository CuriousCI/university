# -*- coding: utf-8 -*-

def decode_XKCD_tuple(xkcd_values: tuple[str, ...], k: int) -> list[int]:
    return sorted(map(decode_value, xkcd_values), reverse=True)[:k]


def decode_value(xkcd: str) -> int:
    # if xkcd in store:
    #     return store[xkcd]
    #

    # weigth, previous, total = "", 0, 0
    #
    # for digit in xkcd[::-1]:
    #     weigth = digit + weigth
    #
    #     if digit != "0":
    #         weigth = int(weigth)
    #         if previous > weigth:
    #             total -= weigth
    #         else:
    #             total += weigth
    #         previous = weigth
    #         weigth = ""

    # store[xkcd] = total

    # return total

    # if xkcd in store:
    #     return store[xkcd]

    # total = list_of_weights_to_number(xkcd_to_list_of_weights(xkcd))
    # store[xkcd] = total
    # return total
    return list_of_weights_to_number(xkcd_to_list_of_weights(xkcd))


def xkcd_to_list_of_weights(xkcd: str) -> list[int]:
    # keys = (
    #     ("1000", "a"),
    #     ("100", "b"),
    #     ("10", "c"),
    #     ("1", "d"),
    #     ("500", "e"),
    #     ("50", "f"),
    #     ("5", "g"),
    # )
    # weigths = {"a": 1000, "b": 100, "c": 10, "d": 1, "e": 500, "f": 50, "g": 5}
    #
    # for weigth, key in keys:
    #     xkcd = xkcd.replace(weigth, key)
    #
    # return [weigths[key] for key in xkcd]

    weigth, weigths = "", []

    for digit in xkcd[::-1]:
        weigth = digit + weigth

        if digit != "0":
            weigths.append(weigth)
            weigth = ""

    return list(map(int, weigths))[::-1]
    # weigths = list(map(int, weigths))
    # weigths.reverse()
    # return weigths

    # keys = (
    #     ("000", "a"),
    #     ("00", "b"),
    #     ("0", "c"),
    # )
    # weigths = {"a": 1000, "b": 100, "c": 10, "1": 1, "5": 1}
    #
    # for weigth, key in keys:
    #     xkcd = xkcd.replace(weigth, key)
    #
    # result = [int(d) * weigths[z] for d, z in zip(xkcd, xkcd[1:]) if d in "15"]
    # if xkcd[-1] in "15":
    #     result.append(int(xkcd[-1]))
    #
    # return result

    # keys = [
    #     ("000", "a"),
    #     ("00", "b"),
    #     ("0", "c"),
    #     ("11", "1d1"),
    #     ("15", "1d5"),
    #     ("51", "5d1"),
    #     ("55", "5d5"),
    # ]
    # weigths = {"a": 1000, "b": 100, "c": 10, "d": 1}
    #
    # for weigth, key in keys:
    #     xkcd = xkcd.replace(weigth, key)
    #
    # result = [int(d) * weigths[z] for d, z in zip(xkcd[::2], xkcd[1::2])]
    # if xkcd[-1] in "15":
    #     result += [int(xkcd[-1])]
    #
    # return result

    # result = []
    # temp = 1
    # for digit in xkcd:
    #     if digit in weigths:
    #         temp = weigths[digit]
    #     else:
    #         result.append(int(digit) * temp)
    #         temp = 1

    # return [weigths[key] for key in xkcd]
    # return result


def list_of_weights_to_number(weigths: list[int]) -> int:
    return sum([-x if x < y else x for x, y in zip(weigths, weigths[1:])]) + weigths[-1]


if __name__ == "__main__":
    pass
