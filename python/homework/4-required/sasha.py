#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def most_frequent_chars(filename: str) -> str:

    finale, origin, parole = '', filename, []

    with open(filename, encoding='utf-8') as file:
        content = file.read().split()
        filename = content[0]
        parole += content[1:]
    while filename != origin:
        with open(filename, encoding='utf-8') as file:
            content = file.read().split()
            filename = content[0]
            parole += content[1:]

            # apertura file ottimizzata
    dict = {}
    for x in range(len(max(parole, key=len))):  # si sposta su colonna (destra sinistra)

        for y in parole:  # si sposta in verticale
            if x < len(y):
                dict[y[x]] = dict.get(y[x], 0)+1

        finale += (sorted(dict.items(),
                   key=lambda x: (-x[1], x[0])))[0][0]
        dict = {}

    # return finale
    return ''
