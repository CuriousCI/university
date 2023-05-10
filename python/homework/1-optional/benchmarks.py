# -*- coding: utf-8 -*-

from timeit import Timer


def a(int_seq: str, subtotal: int) -> int:
    numbers = [int(number) for number in int_seq.split(',')]

    valid_substrings, tail, total = 0, 0, 0

    for head in numbers:
        total += head

        while total > subtotal:
            total -= numbers[tail]
            tail += 1

        if total == subtotal:
            valid_substrings += 1
            leading_zeros = tail

            while numbers[leading_zeros] == 0:
                valid_substrings += 1
                leading_zeros += 1

    return valid_substrings


def b(int_seq: str, subtotal: int) -> int:
    numbers = [int(number) for number in int_seq.split(',')]

    valid_substrings, tail, total, zeros = 0, 0, 0, 0

    for head in numbers:
        total += head

        if head:
            zeros = 0

        while total > subtotal:
            total -= numbers[tail]
            tail += 1

        if total == subtotal:
            if not zeros and not numbers[tail]:
                leading_zeros = tail
                while not numbers[leading_zeros]:
                    zeros += 1
                    leading_zeros += 1
            valid_substrings += 1 + zeros

    return valid_substrings


def c(int_seq: str, subtotal: int) -> int:
    numbers = [*map(int, int_seq.split(','))]

    valid_substrings, tail, total, zeros = 0, 0, 0, 0

    for head in numbers:
        total += head

        if head:
            zeros = 0

        while total > subtotal:
            total -= numbers[tail]
            tail += 1

        if total == subtotal:
            if not zeros and not numbers[tail]:
                leading_zeros = tail
                while not numbers[leading_zeros]:
                    zeros += 1
                    leading_zeros += 1
            valid_substrings += 1 + zeros

    return valid_substrings


def d(int_seq: str, subtotal: int) -> int:
    numbers = [*map(int, int_seq.split(','))]

    valid_substrings, tail, segment, zeros = 0, 0, 0, 0

    for number in numbers:
        segment += number

        if number:
            zeros = 0

        while segment > subtotal:
            segment -= numbers[tail]
            tail += 1

        if segment == subtotal:
            if not zeros and not numbers[tail]:
                leading_zeros = tail
                while not numbers[leading_zeros]:
                    zeros += 1
                    leading_zeros += 1
            valid_substrings += 1 + zeros

    return valid_substrings


def e(int_seq: str, subtotal: int) -> int:
    numbers = [*map(int, int_seq.split(','))]

    valid_substrings, tail, segment, zeros = 0, 0, 0, 0

    for number in numbers:
        segment += number

        while segment > subtotal:
            if zeros:
                tail += zeros
                zeros = 0
            segment -= numbers[tail]
            tail += 1

        if segment == subtotal:
            if numbers[tail]:
                zeros = 0
            elif not zeros:
                leading_zeros = tail + 1
                while not numbers[leading_zeros]:
                    leading_zeros += 1
                zeros = leading_zeros - tail
            valid_substrings += 1 + zeros

    return valid_substrings


if __name__ == '__main__':
    functions = [('a', a), ('b', b), ('c', c), ('d', d), ('e', e)]
    inputs = [
        ('3,0,4,0,3,1,0,10,0,1,0,0,5,0,4,2' * 1000, 9),
        ('1,' * 1000 + '0', 1),
        ('0,'*1000 + '2,' + '0,'*500 + '2', 2)
    ]

    for string, subtotal in inputs:
        for name, function in functions:
            print(name, Timer(lambda: function(string, subtotal)).repeat(1, 100))
        print()
