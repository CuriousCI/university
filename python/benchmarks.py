# -*- coding: utf-8 -*-

from timeit import Timer
# from program01 import ...

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
    )

    inputs = (
    )

    cumulative_time = {}
    studied_function = None

    for args in inputs:
        print(f'{fg(184, 187, 38)}{args[0]}{RESET}')

        for function in functions:
            time = min(Timer(lambda: function(*args)).repeat(50, 1))
            if function == studied_function:
                print(f'{BOLD}{ITALIC}{UNDERLINE}{time}{RESET}')
            else:
                print(time)

            cumulative_time[function] = cumulative_time.get(function, 0) + time
        print()

    best_time = min(cumulative_time.values())
    worst_time = max(cumulative_time.values())
    time_difference = worst_time - best_time
    relative_time_difference = time_difference / min_time * 100

    print(f'{fg(184, 187, 38)}Cumulative times{RESET}')
    print(f'{fg(184, 187, 38)}D:{RESET} {time_difference}')
    print(f'{fg(184, 187, 38)}%:{RESET} {relative_time_difference:.2f}%')

    for function in functions:
        time = cumulative_time[function]
        if time == best_time:
            print(f'{fg(250, 189, 47)}{time}{RESET}')
        elif time == worst_time:
            print(f'{fg(251, 73, 52)}{time}{RESET}')
        else:
            print(time)

    edge_cases = (
    )

    for args in edge_cases:
        for function in functions:
            print(function(edge_cases))
        print()
