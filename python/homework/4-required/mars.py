#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def most_frequent_chars(filename: str) -> str:
    first_file, words = filename, []

    # words_counter, length = {}, 0
    words = []
    while True:
        with open(filename, encoding='utf_8') as file:
            filename = file.readline().strip()
            words.extend(file.read().split())
            # for word in file.read().split():
            #     if word in words_counter:
            #         words_counter[word] += 1
            #     else:
            #         words_counter[word] = 1

        if filename == first_file:
            break

    print('unique words', len(words), 'vs', len(set(words)))
    print('unique lengths', len(set(map(len, words))))
    print('words length', len(''.join(words)))
    print('unique words length', len(''.join(list(set(words)))))
    print('max length', max(set(map(len, words))))
    print('min length', min(set(map(len, words))))
    print('unique letters', len(set(''.join(words))))

    # length = len(max(words_counter, key=len))
    # results = [{} for _ in range(length)]
    #
    # for word in words_counter:
    #     for index, letter in enumerate(word):
    #         if letter in results[index]:
    #             results[index][letter] += words_counter[word]
    #         else:
    #             results[index][letter] = words_counter[word]
    #
    # return ''.join([min(frequencies.items(), key=swap)[0] for frequencies in results])


def swap(frequency): return (-frequency[1], frequency[0])


if __name__ == '__main__':
    print(most_frequent_chars('test01/A.txt'))
    pass
