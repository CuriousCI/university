from math import log10
from timeit import Timer


def list_find(nth: int) -> str:
    return ''.join([str(x) for x in range(1, int(nth / 1.7))])[nth - 1]


def find_nth_char(nth: int) -> str:
    length, number = 0, 0

    while length < nth:
        number += 1
        offset = len(str(number))

        if length + offset > nth:
            return str(number)[nth - length - 1]

        length += offset

    return '0'


# assert find_nth_char(200) == list_find(
#     200), f'Expected {find_nth_char(200)} found {list_find(200)}'
# assert find_nth_char(300) == list_find(
#     300), f'Expected {find_nth_char(300)} found {list_find(300)}'
#
# assert find_nth_char(1230) == list_find(
#     1230), f'Expected {find_nth_char(1230)} found {list_find(1230}'


# bench1 = Timer(lambda: list_find(300)).repeat(1, 10000)
# bench2 = Timer(lambda: find_nth_char(300)).repeat(1, 10000)
#
#
# print(f'{bench1} VS {bench2}')

print(log10(200))
