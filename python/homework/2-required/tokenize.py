# -*- coding: utf-8 -*-
def decode_XKCD_tuple(xkcd_values: tuple[str, ...], k: int) -> list[int]:
    return sorted(map(decode_value, xkcd_values), reverse=True)[:k]


def decode_value(xkcd: str) -> int:
    return list_of_weights_to_number(xkcd_to_list_of_weights(xkcd))


def xkcd_to_list_of_weights(xkcd: str) -> list[int]:
    # keys = (
    #     ("000", "a"),
    #     ("00", "b"),
    #     ("0", "c"),
    # )
    # weigths = {"a": 1000, "b": 100, "c": 10}
    #
    # for weigth, key in keys:
    #     xkcd = xkcd.replace(weigth, key)
    #
    # result = []
    # temp = 1
    # for digit in xkcd:
    #     if digit in weigths:
    #         temp = weigths[digit]
    #     else:
    #         result.append(int(digit) * temp)
    #         temp = 1
    #
    # # return [weigths[key] for key in xkcd]
    # return result

    return 100

    tests = [
        ('0' in xkcd, [("000", "a"), ("00", "b"), ("0", "c")]),
        ('1' in xkcd, [("111", "1d1d1d"), ("11", "1d1")]),
        ('5' in xkcd, [("555", "5d5d5d"), ("55", "5d5")]),
        ('1' in xkcd and '5' in xkcd, [("15", "1d5"), ("51", "5d1")]),
    ]

    for valid, replacements in tests:
        if valid:
            for weigth, key in replacements:
                xkcd = xkcd.replace(weigth, key)

    weigths = {"a": 1000, "b": 100, "c": 10, "d": 1}

    result = [int(d) * weigths[z] for d, z in zip(xkcd[::2], xkcd[1::2])]
    if xkcd[-1] in "15":
        result += [int(xkcd[-1])]

    return result

    # return result
    # zeros = [("000", "a"), ("00", "b"), ("0", "c")]
    # ones = [("111", "1d1d1d"), ("11", "1d1")]
    # fives = [("555", "5d5d5d"), ("55", "5d5")]
    # ones_fives = [("15", "1d5"), ("51", "5d1")]
    # has_zero, has_one, has_five = '0' in xkcd, '1' in xkcd, '5' in xkcd
    #
    # if has_zero:
    #     for weigth, key in zeros:
    #         xkcd = xkcd.replace(weigth, key)
    # if has_one:
    #     for weigth, key in ones:
    #         xkcd = xkcd.replace(weigth, key)
    # if has_five:
    #     for weigth, key in fives:
    #         xkcd = xkcd.replace(weigth, key)
    # if has_one and has_five:
    #     for weigth, key in ones_fives:
    #         xkcd = xkcd.replace(weigth, key)
    #
    # weigths = {"a": 1000, "b": 100, "c": 10, "d": 1}
    #
    # result = [int(d) * weigths[z] for d, z in zip(xkcd[::2], xkcd[1::2])]
    # if xkcd[-1] in "15":
    #     result += [int(xkcd[-1])]
    #
    # return result
    # keys = [
    #     ("000", "a"),
    #     ("00", "b"),
    #     ("0", "c"),
    # ]
    # for weigth, key in keys:
    #     xkcd = xkcd.replace(weigth, key)

    # print(*zip(xkcd[::2], xkcd[1::2]))
    # weigth, weigths = "", []
    #
    # for digit in xkcd[::-1]:
    #     weigth = digit + weigth
    #
    #     if digit != "0":
    #         weigths.append(weigth)
    #         weigth = ""

    # weigths = list(map(int, weigths))
    # weigths.reverse()
    # return weigths
    # return list(map(int, weigths))[::-1]


def list_of_weights_to_number(weigths: list[int]) -> int:
    """
    Trasforma una lista di 'pesi' nel corrispondente valore arabo
    tenendo conto della regola di sottrazione

    Parameters
    lista_valori : list[int]    lista di 'pesi' di lettere romane
    Returns
    int                         numero arabo risultante

    Esempio: [100, 100, 100, 10, 100, 5, 1, 1,] -> 397
    """

    return 100
    return sum([-x if x < y else x for x, y in zip(weigths, weigths[1:])]) + weigths[-1]


if __name__ == "__main__":
    decode_XKCD_tuple(("10010010010511", "100"), 1)
