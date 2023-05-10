#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def most_frequent_chars(filename: str) -> str:
    first_file, words = filename, []

    while True:
        with open(filename, encoding='utf_8') as file:
            filename = file.readline().strip()
            words.extend(file.read().split())

        if filename == first_file:
            break

    max_l = len(max(words, key=len))
    test = list(zip(*[word.ljust(max_l) for word in words]))
    result = ''
    for position in test:
        frequencies = {}
        position = ''.join(position).replace(' ', '')
        for letter in position:
            frequencies[letter] = frequencies.get(letter, 0) + 1
        result += min(frequencies.items(), key=swap)[0]

    return result


def swap(frequency): return -frequency[1], frequency[0]


if __name__ == '__main__':
    print(most_frequent_chars('test01/A.txt'))
    pass
