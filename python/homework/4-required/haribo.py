#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import defaultdict


def swap(count): return (-count[1], count[0])


def most_frequent_chars(filename: str) -> str:
    first, words = filename, defaultdict(int)

    while True:
        with open(filename, encoding='utf_8') as file:
            filename = file.readline().strip()

            for word in file.read().split():
                words[word] += 1

        if filename == first:
            break

    counters = [defaultdict(int) for _ in range(len(max(words, key=len)))]

    for word, count in words.items():
        for counter, letter in zip(counters, word):
            counter[letter] += count

    return ''.join([min(counter.items(), key=swap)[0] for counter in counters])


if __name__ == '__main__':
    pass
