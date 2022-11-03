# import datetime
from datetime import date

# Cubic root


def cubic_root(number: float) -> float:
    return number**(1/3)


print(f'Radice cubica di 10: {cubic_root(10)}',
      f'Radice cubica di 20012.12: {cubic_root(20012.12)}',
      f'Radice cubica di 8: {cubic_root(8)}', sep='\n')


# Quadratic formula


def quadratic_formula(a: float, b: float, c: float) -> (float, float):
    # If delta < 0, delta**.5 becomes a 'complex number'
    delta = b**2 - 4*a*c

    if delta < 0:
        raise ValueError('Delta is negative')

    return (-b + delta**.5) / 2*a, (-b - delta**.5) / 2*a


try:
    print(f'"Parabola" del pasotre Gianni: {quadratic_formula(10, 10, -10)[0]}',
          f'"Parabola" del pasotre Carlucci: {quadratic_formula(2, 0, -4)[0]}',
          f'"Parabola" di Carlucci e Gianni: {quadratic_formula(2, 0, -4)}', sep='\n')
except ValueError:
    print('Delta is negative')


# Odd & Even


def odd_even() -> int:
    numbers = [int(input()) for _ in range(5)]
    # return sum(map(lambda x: -x if x & 1 else x, numbers))
    return sum(map(lambda x: x * (((x & 1) * -2) + 1), numbers))


print(f'Il pastore Carlucci conta i "piedi" delle pecore: {odd_even()}')


# Exam grades


def sum_grades() -> int:
    grades = [int(input()) for _ in range(3)]
    are_grades_valid = all(map(lambda grade: 0 <= grade <= 30, grades))

    if not are_grades_valid:
        raise ValueError('Almeno uno dei voti non e\' valido!')

    return sum(grades)


try:
    print(f'Devi passare l\'esame! {sum_grades()}')
except ValueError as error:
    print(error)


# Trouble Double Dates


def is_date_valid(day: int, month: int, year: int) -> bool:
    try:
        # I'm too lazy to check it myself
        date(year, month, day)
    except Exception:
        return False

    return True


print(f'Sei sicuro di conoscere le date? {is_date_valid(10, 10, 2022)}',
      f'Hmmm... : {is_date_valid(210, 10, -20)}', sep='\n')


# Strip, but worse...


def fake_strip(string: str) -> str:
    start, end = 0, len(string)

    for (index, character) in enumerate(string):
        if not character.isspace():
            start = index
            break

    for (index, character) in enumerate(string[::-1]):
        if not character.isspace():
            end = index
            break

    return string[start:len(string) - end]

# TODO fix this problem


text = '\n   \t Hello, World!    \t\n'
assert text.strip() == fake_strip(text), 'Il tuo codice non funziona!'


# Do I really have to greet you?


def greet() -> str:
    return f'Ciao {input()}\nBuona Giornata!'


print(greet())
