#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def most_frequent_chars(filename: str) -> str:
    return "".join(map(lambda d: min(d, key=lambda char: (-d[char], char)), process(read_chained_file(filename, filename))))


def read_chained_file(first_file: str, current_file: str) -> list:
    with open(current_file, encoding='utf-8') as file:
        new_file = file.readline().strip()
        result = file.read().split()

    if new_file != first_file:
        result.extend(read_chained_file(first_file, new_file))

    return result


def process(words):
    dicts = []
    len_dicts = 0

    for word in words:
        for curr_pos, char in enumerate(word):
            if curr_pos < len_dicts:
                curr_dict = dicts[curr_pos]
                curr_dict[char] = curr_dict.get(char, 0)+1
            else:
                dicts.append({char: 1})

                len_dicts += 1
    return dicts

# new_file, result = clear_file_text(
#     open(current_file, encoding="utf-8").read())
# if new_file != first_file:
#     result.extend(read_chained_file(first_file, new_file))
# def clear_file_text(file_text: str) -> tuple[str, list]:
#     strings = file_text.split()
#     return strings.pop(0), strings
# def clear_file_text(file_text: str) -> tuple[str, str]:
#     strings = file_text.split()
#     return strings.pop(0), strings
