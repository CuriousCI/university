#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def reduce(counter: dict[str, int]) -> str:
    return min([(-count, letter) for letter, count in counter.items()])[1]


def most_frequent_chars(filename: str) -> str:
    first, words = filename, []

    while True:
        with open(filename, encoding='utf_8') as file:
            filename = file.readline().strip()
            words.extend(file.read().split())

        if filename == first:
            break

    counters = [{} for _ in range(len(max(words, key=len)))]

    for word in words:
        for counter, letter in zip(counters, word):
            if letter in counter:
                counter[letter] += 1
            else:
                counter[letter] = 1

    return ''.join([reduce(counter) for counter in counters])


if __name__ == '__main__':
    pass

    # for word in file.read().split():
    # words[word] = words[word] + 1 if word in words else 1

    # counter[letter] = counter[letter] + 1 if letter in counter else 1

# words.extend(file.read().split())
# if letter in counter:
#     counter[letter] += 1
# else:
#     counter[letter] = 1

# for word in words:
# if word in words:
#     words[word] += 1
# else:
#     words[word] = 1
