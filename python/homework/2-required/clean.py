# -*- coding: utf-8 -*-


def decode_XKCD_tuple(xkcd_values: tuple[str, ...], k: int) -> list[int]:
    return sorted(map(decode_value, xkcd_values), reverse=True)[:k]


def decode_value(xkcd: str) -> int:
    return list_of_weights_to_number(xkcd_to_list_of_weights(xkcd))


def xkcd_to_list_of_weights(xkcd: str) -> list[int]:
    keys = (("1000", "a"), ("100", "b"), ("10", "c"),
            ("1", "d"), ("500", "e"), ("50", "f"), ("5", "g"))
    weigths = {"a": 1000, "b": 100, "c": 10, "d": 1, "e": 500, "f": 50, "g": 5}

    for weigth, key in keys:
        xkcd = xkcd.replace(weigth, key)

    return [weigths[key] for key in xkcd]


def list_of_weights_to_number(weigths: list[int]) -> int:
    return sum([-x if x < y else x for x, y in zip(weigths, weigths[1:])]) + weigths[-1]


if __name__ == "__main__":
    pass
