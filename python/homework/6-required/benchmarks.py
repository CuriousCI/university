# -*- coding: utf-8 -*-

from piolo import generate_snake as piolo
from giak import generate_snake as giak
from baki import generate_snake as baki
from souleater import generate_snake as souleater
from nogamenolife import generate_snake as nogamenolife
from onepiece import generate_snake as onepiece
from bleach import generate_snake as bleach
from naruto import generate_snake as naruto
from haikyuu import generate_snake as haikyuu
from fastest import generate_snake as fastest
from acsai import generate_snake as acsai
from program01 import generate_snake
from timeit import Timer
import json

ESC = '\x1B'
CSI = f'{ESC}['
RESET = f'{CSI}m'
BOLD = f'{CSI}1m'
ITALIC = f'{CSI}3m'
UNDERLINE = f'{CSI}4m'


def foreground(red, green, blue):
    return f'{CSI}38;2;{red};{green};{blue}m'


def background(red, green, blue):
    return f'{CSI}48;2;{red};{green};{blue}m'


if __name__ == "__main__":
    functions = (
        # generate_snake,
        # haikyuu,
        # naruto,
        baki,
        # acsai,
        fastest,
        # souleater,
        # bleach,
        # onepiece,
        # nogamenolife,
        # giak,
        # piolo,
    )

    files = (
        './data/input_00.json',
        './data/input_01.json',
        './data/input_02.json',
        './data/input_03.json',
        './data/input_04.json',
        './data/input_05.json',
        './data/input_06.json',
        './data/input_07.json',
        './data/input_08.json',
        './data/input_09.json',
        './data/input_10.json',
        './secrets/input_00.json',
        './secrets/input_01.json',
        './secrets/input_02.json',
        './secrets/input_03.json',
        './secrets/input_04.json',
        './secrets/input_05.json',
        './secrets/input_06.json',
        './secrets/input_07.json',
        './secrets/input_08.json',
        './secrets/input_09.json',
    )

    inputs = [
        ['data/input_00.png', [12, 13], 'SW W N S SW', 'output/output_end_00.png'],
    ]

    for file in files:
        with open(file) as file:
            data = json.load(file)['input']

        inputs.append([data['start_img'], data['position'],
                      data['commands'], data['out_img']])

    cumulative_times = {}
    current_function = baki

    for args in inputs:
        print(f'{foreground(184, 187, 38)}{args[0]}{RESET}')
        for function in functions:
            # print(function.__name__, end=': ')
            time = Timer(lambda: function(*args)).repeat(50, 1)
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
    print(f'{foreground(184, 187, 38)}Cumulative times{RESET}')
    print(f'{foreground(184, 187, 38)}Delta time:{RESET} {max_time - min_time}')
    percent = "{:.2f}".format((max_time - min_time) / min_time * 100)
    print(f'{foreground(184, 187, 38)}Relative delta:{RESET} {percent}%')
    for function in functions:
        time = cumulative_times[function]
        if time == min_time:
            print(f'{foreground(250, 189, 47)}{time}{RESET}')
        elif time == max_time:
            print(f'{foreground(251, 73, 52)}{time}{RESET}')
        else:
            print(time)

    edge_cases = (
        # ['param1', 'param2', 'etc...'],
    )

    for args in edge_cases:
        for function in functions:
            print(function(edge_cases))
        print()
