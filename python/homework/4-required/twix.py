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

    words.sort(key=len, reverse=True)
    length = len(words[0])

    result = ''

    for index in range(length):
        frequencies = {}
        for word in words:
            if index >= len(word):
                break
            letter = word[index]
            if letter in frequencies:
                frequencies[letter] += 1
            else:
                frequencies[letter] = 1

            # frequencies[letter] = frequencies.get(letter, 0) + 1

        result += min(frequencies.items(), key=swap)[0]

    return result


def swap(frequency): return (-frequency[1], frequency[0])


if __name__ == '__main__':
    print(most_frequent_chars('test01/A.txt'))
    pass
