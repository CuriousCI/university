#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def reduce(counter):
    return min([(-count, letter) for letter, count in counter.items()])[1]


def most_frequent_chars(filename: str) -> str:
    first_file, words = filename, {}

    while True:
        with open(filename, encoding='utf-8') as file:
            filename = file.readline().strip()
            for word in file.read().split():
                words[word] = words.get(word, 0) + 1

            if filename == first_file:
                break

    counters = [{} for _ in max(words, key=len)]

    for word, count in words.items():
        for counter, letter in zip(counters, word):
            counter[letter] = counter.get(letter, 0) + count

    return ''.join(map(reduce, counters))
