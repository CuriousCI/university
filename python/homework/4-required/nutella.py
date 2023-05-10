#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def most_frequent_chars(filename: str) -> str:
    first_file, words = filename, {}

    while True:
        with open(filename, encoding='utf_8') as file:
            filename = file.readline().strip()
            for word in file.read().split():
                if word in words:
                    words[word] += 1
                else:
                    words[word] = 1

        if filename == first_file:
            break

    positions = [{} for _ in range(len(max(words, key=len)))]

    for word in words:
        for position, letter in enumerate(word):
            if letter in positions[position]:
                positions[position][letter] += words[word]
            else:
                positions[position][letter] = words[word]

    return ''.join([min(frequencies.items(), key=swap)[0] for frequencies in positions])


def swap(frequency): return (-frequency[1], frequency[0])


if __name__ == '__main__':
    print(most_frequent_chars('test01/A.txt'))
    pass
