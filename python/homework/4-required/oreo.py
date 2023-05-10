#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def most_frequent_chars(filename: str) -> str:
    first_file = filename
    visited = False
    content: str = ''

    while not visited:
        with open(filename, encoding='utf-8') as file:
            filename = file.readline().strip()
            content += file.read()

        if filename == first_file:
            visited = True

    words = content.split()
    words.sort(key=len, reverse=True)
    length = len(words[0])

    result = ''

    for index in range(length):
        frequencies: dict[str, int] = {}
        for word in words:
            if index >= len(word):
                break
            letter = word[index]
            if letter in frequencies:
                frequencies[letter] += 1
            else:
                frequencies[letter] = 1

        result += min(frequencies.items(), key=swap)[0]

    return result


def swap(x):
    return (-x[1], x[0])


if __name__ == '__main__':
    print(most_frequent_chars('test02/bullfight.txt'))
    pass
