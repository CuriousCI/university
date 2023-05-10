# -*- coding: utf-8 -*-

from timeit import Timer
from program01 import ex1
from lockness import ex1 as lockness
from topg import ex1 as topg
from general import ex1 as general


if __name__ == "__main__":
    functions = (
        ex1,
        lockness,
        topg,
        general,
    )

    inputs = (
        ['ft1.txt', 2, 4, 20],
        ['ft2.txt', 2, 5, 10],
        ['ft100.txt', 23, 49, 17],
        ['ft1100.txt', 10, 29, 24],
        ['ft1600.txt', 6, 51, 40],
        ['ft2100.txt', 11, 56, 36],
        ['ft2600.txt', 8, 36, 17],
        ['ft3100.txt', 19, 43, 22],
        ['ft3600.txt', 5, 39, 35],
    )

    for args in inputs:
        for function in functions:
            time = Timer(lambda: function(*args)).repeat(1, 2)
            print(time)
        print()

    edge_cases = (
        # ['param1', 'param2', 'etc...'],
    )

    for args in edge_cases:
        for function in functions:
            print(function(edge_cases))
        print()
