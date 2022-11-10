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
        # ['param1', 'param2', 'etc...'],
    )

    for args in inputs:
        for function in functions:
            time = Timer(lambda: function(*args)).repeat(1, 10)
            print(time)
        print()

    edge_cases = (
        # ['param1', 'param2', 'etc...'],
    )

    for args in edge_cases:
        for function in functions:
            print(function(edge_cases))
        print()
