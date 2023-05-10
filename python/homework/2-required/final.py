# -*- coding: utf-8 -*-

def decode_XKCD_tuple(xkcd_values: tuple[str, ...], k: int) -> list[int]:
    return sorted(map(decode_value, xkcd_values), reverse=True)[:k]


def decode_value(xkcd: str) -> int:
    if len(xkcd) < 100:
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

    return list_of_weights_to_number(xkcd_to_list_of_weights(xkcd))


def xkcd_to_list_of_weights(xkcd: str) -> list[int]:
    return list(map(int, xkcd.replace("5", ",5").replace("1", ",1")[1:].split(",")))


def list_of_weights_to_number(weigths: list[int]) -> int:
    if len(weigths) < 100:
        total = 0

        for index in range(len(weigths) - 1):
            if weigths[index] < weigths[index + 1]:
                total -= weigths[index]
            else:
                total += weigths[index]

        return total + weigths[-1]

    return sum([-x if x < y else x for x, y in zip(weigths, weigths[1:])]) + weigths[-1]


if __name__ == "__main__":
    pass
