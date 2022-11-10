# -*- coding: utf-8 -*-

from timeit import Timer
from program01 import most_frequent_chars
# from filename import another_function as fname


if __name__ == "__main__":
    functions = (
        most_frequent_chars,
        # fname
    )

    inputs = (
        ['test01/A.txt'],
        ['test02/bullfight.txt'],
        ['test03/woodchuck.txt'],
        ['test04/pampers.txt'],
        ['test05/avocados.txt'],
        ['test06/strums.txt'],
        ['test07/sinew.txt'],
        ['test08/boilings.txt'],
        ['test09/meddles.txt'],
        ['test10/aileron.txt'],
    )

    for args in inputs:
        for function in functions:
            time = Timer(lambda: function(*args)).repeat(1, 10)
            print(time)
        print()

    edge_cases = (
    )

    for args in edge_cases:
        for function in functions:
            print(function(edge_cases))
        print()
