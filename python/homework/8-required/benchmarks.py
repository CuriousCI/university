# -*- coding: utf-8 -*-

from timeit import Timer
from program01 import dumbothello
from chonji import dumbothello as chonji
from dangun import dumbothello as dangun
from dosan import dumbothello as dosan
from wonhyo import dumbothello as wonhyo
from yulgok import dumbothello as yulgok
from joonggun import dumbothello as joonggun
from toigae import dumbothello as toigae
from hwarang import dumbothello as hwarang
from choongmoo import dumbothello as choongmoo
from kwanggae import dumbothello as kwanggae
from poeun import dumbothello as poeun
from giak import dumbothello as giak
from giak2 import dumbothello as giak2
from dav import dumbothello as dav
from flag import dumbothello as flag
from flag2 import dumbothello as flag2
from andrea import dumbothello as andrea
from andrea2 import dumbothello as andrea2
from test import dumbothello as test


ESC = '\x1B'
CSI = f'{ESC}['
RESET = f'{CSI}m'
BOLD = f'{CSI}1m'
ITALIC = f'{CSI}3m'
UNDERLINE = f'{CSI}4m'


def fg(red, green, blue):
    return f'{CSI}38;2;{red};{green};{blue}m'


def bg(red, green, blue):
    return f'{CSI}48;2;{red};{green};{blue}m'


if __name__ == "__main__":
    functions = (
        # dumbothello,
        # chonji,
        # dangun,
        # dosan,
        # wonhyo,
        # yulgok,
        # joonggun,
        # toigae,
        # hwarang,
        # choongmoo,
        # kwanggae,
        poeun,
        test,
        # giak,
        # giak2,
        # dav,
        # flag,
        # flag2,
        # andrea,
        # andrea2,
    )

    inputs = (
        ['boards/01.txt'],
        ['boards/02.txt'],
        ['boards/03.txt'],
        ['boards/04.txt'],
        ['boards/05.txt'],
        ['boards/06.txt'],
        ['boards/07.txt'],
        ['boards/08.txt'],
        ['boards/09.txt'],
        # ['small.txt'],
        # ['medium.txt'],
        # ['large.txt'],
    )

    cumulative_times = {}
    current_function = kwanggae

    for args in inputs:
        print(f'{fg(184, 187, 38)}{args[0]}{RESET}')
        for function in functions:
            # print(function.__name__, end=': ')
            time = Timer(lambda: function(*args)).repeat(5, 1)
            time = min(time)
            if function == current_function:
                print(f'{BOLD}{ITALIC}{UNDERLINE}{time}{RESET}')
            else:
                print(time)
            cumulative_times[function] = cumulative_times.get(
                function, 0) + time
        print()

    min_time = min(cumulative_times.values())
    max_time = max(cumulative_times.values())
    print(f'{fg(184, 187, 38)}Cumulative times{RESET}')
    print(f'{fg(184, 187, 38)}Delta time:{RESET} {max_time - min_time}')
    percent = "{:.2f}".format((max_time - min_time) / min_time * 100)
    print(f'{fg(184, 187, 38)}Relative delta:{RESET} {percent}%')
    for function in functions:
        time = cumulative_times[function]
        if time == min_time:
            print(f'{fg(250, 189, 47)}{time}{RESET}')
        elif time == max_time:
            print(f'{fg(251, 73, 52)}{time}{RESET}')
        else:
            print(time)

    edge_cases = (
        ['empty.txt'],
        ['black.txt'],
        ['white.txt'],
        # ['param1', 'param2', 'etc...'],
    )

    print('\n')
    for args in edge_cases:
        for function in functions:
            print(function(*args))
        print()
