# -*- coding: utf-8 -*-

def ex1(int_seq, subtotal):
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
    pass
