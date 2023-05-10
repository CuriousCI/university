# -*- coding: utf-8 -*-

from timeit import Timer
from program01 import most_frequent_chars
from mars import most_frequent_chars as mars
from snikers import most_frequent_chars as snikers
from bueno import most_frequent_chars as bueno
from ferrero import most_frequent_chars as ferrero
from haribo import most_frequent_chars as haribo
from mms import most_frequent_chars as mms
from nutella import most_frequent_chars as nutella
from kinder import most_frequent_chars as kinder
from twix import most_frequent_chars as twix
from kitkat import most_frequent_chars as kitkat
from oreo import most_frequent_chars as oreo
from ringo import most_frequent_chars as ringo
from giak import most_frequent_chars as giak
from ph04 import most_frequent_chars as ph04
from ph04opt import most_frequent_chars as ph04opt
from ph04v2 import most_frequent_chars as ph04v2
from ph04v2i import most_frequent_chars as ph04v2i
from ph04v3 import most_frequent_chars as ph04v3
from tarr import most_frequent_chars as tarr
from tarrv2 import most_frequent_chars as tarrv2
from tarrv3 import most_frequent_chars as tarrv3
from tarrv4 import most_frequent_chars as tarrv4
from tarrv5 import most_frequent_chars as tarrv5
from tarrv6 import most_frequent_chars as tarrv6
from tarrv7 import most_frequent_chars as tarrv7
from sasha import most_frequent_chars as sasha
from sashav2 import most_frequent_chars as sashav2


if __name__ == "__main__":
    functions = (
        # most_frequent_chars,
        # mars,
        snikers,
        ferrero,
        # bueno,
        # haribo,
        # mms,
        # nutella,
        # kinder,
        # twix,
        # kitkat,
        # oreo,
        # ringo,
        # giak,
        # ph04,
        # ph04opt,
        # ph04v2,
        # ph04v2i,
        # ph04v3,
        # tarr,
        # tarrv2,
        # tarrv3,
        # tarrv4,
        # tarrv5,
        # tarrv6,
        # tarrv7,
        # sasha,
        # sashav2,
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
        ['test11/metonymies.txt'],
        ['test12/incipience.txt'],
        # ['test13/big.txt'],
    )

    for args in inputs:
        for function in functions:
            time = Timer(lambda: function(*args)).repeat(1, 1)
            print(time)
        print()

    edge_cases = (
    )

    for args in edge_cases:
        for function in functions:
            print(function(edge_cases))
        print()
