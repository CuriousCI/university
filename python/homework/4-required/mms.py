#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def swap(count): return (-count[1], count[0])


def most_frequent_chars(filename: str) -> str:
    first_file, words_counter = filename, {}

    while True:
        with open(filename, encoding='utf_8') as file:
            filename = file.readline().strip()
            for word in file.read().split():
                if word in words_counter:
                    words_counter[word] += 1
                else:
                    words_counter[word] = 1

        if filename == first_file:
            break

    counters = [{} for _ in range(len(max(words_counter, key=len)))]

    for word in words_counter:
        for position, letter in enumerate(word):
            if letter in counters[position]:
                counters[position][letter] += words_counter[word]
            else:
                counters[position][letter] = words_counter[word]

    return ''.join([min(counter.items(), key=swap)[0] for counter in counters])


if __name__ == '__main__':
    pass
