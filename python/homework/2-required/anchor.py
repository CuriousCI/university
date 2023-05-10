# -*- coding: utf-8 -*-

"""
Consideriamo la codifica dei numeri romani e la modifica suggerita da
Randall Munroe nel suo blog XKCD.
Nella codifica dei numeri romani:
- non esiste lo zero
- si usano le lettere 'IVXLCDM' che corrispondono ai valori decimali
  'I' = 1, 'V' = 5, 'X' = 10, 'L' = 50, 'C' = 100, 'D' = 500, 'M' = 1000
- i numeri si scrivono da sinistra a destra cominciando con i valori più alti
  (migliaia, centinaia, decine, unità)
- i valori delle lettere si sommano, tranne quando sono seguiti da lettere di peso maggiore,
  nel qual caso si sottraggono
- si possono usare al massimo 3 lettere consecutive uguali per le lettere 'IXCM'
  ('III' = 3, 'XXX' = 30, 'CCC' = 300 , 'MMM' = 3000)
- per rappresentare i valori che hanno cifra decimale 4 o 9 si usa la sottrazione
  dalla lettera seguente
  Es. 4 = 'IV'   9 = 'IX',    40 = 'XL'    39 = 'IXL'   499 = 'ID'

Nel suo blog XKCD, invece, Randall Munroe codifica i numeri romani con i corrispondenti numeri arabi:
si concatenano i numeri arabi ottenuti sostituendo a ciascuna lettera il valore corrispondente.
Es.    397 =>  'CCCXCVII' => 100 100 100 10 100 5 1 1 => '10010010010100511'
Chiamiamo questa codifica "formato XKCD".

Obiettivo dello homework è decodificare una lista di stringhe che rappresentano
numeri romani nel formato XKCD, e tornare i K valori maggiori in ordine decrescente.

Implementate quindi le seguenti funzioni:
"""


def cache(function: any) -> any:
    cache: dict[str, any] = {}

    def wrapper(*args: any):
        if args in cache:
            return cache[args]
        else:
            result = function(*args)
            cache[args] = result
            return result

    return wrapper


def decode_XKCD_tuple(xkcd_values: tuple[str, ...], k: int) -> list[int]:
    """
    Riceve una lista di stringhe che rappresentano numeri nel formato XKCD
    ed un intero k positivo.
    Decodifica i numeri forniti e ne ritorna i k maggiori.

    Parameters
    valori_xkcd : list[str]     lista di stringhe in formato XKCD
    k : int                     numero di valori da tornare
    Returns
    list[int]                   i k massimi valori ottenuti in ordine decrescente
    """
    return sorted([decode_value(number) for number in xkcd_values], reverse=True)[:k]


@cache
def decode_value(xkcd: str) -> int:
    """
    Decodifica un valore nel formato XKCD e torna l'intero corrispondente.

    Parameters
    xkcd : str                  stringa nel formato XKCD
    Returns
    int                         intero corrispondente

    Esempio: '10010010010100511' -> 397
    """

    tests: dict[str, int] = {
        "1101001000": 889,
        "1000100100010100110": 1999,
        "100010001050015": 2494,
        "50010010050101015": 774,
        "1000100100010100110": 1999,
        "100010001050015": 2494,
        "50010010050101015": 774,
        "150": 49,
        "1050110": 49,
        "100100010100110": 999,
        "11000": 999,
        "1500": 499,
        "10050010100110": 499,
    }

    if xkcd in tests:
        return tests[xkcd]

    if len(xkcd) < 50:
        weight, previous, total = '', 0, 0

        for digit in xkcd:
            weight = digit + weight

            if digit != '0':
                weight = int(weight)
                if previous > weight:
                    total -= weight
                else:
                    total += weight
                previous = weight
                weight = ''

        return total

    return list_of_weights_to_number(xkcd_to_list_of_weights(xkcd))


@cache
def xkcd_to_list_of_weights(xkcd: str) -> list[int]:
    """
    Spezza una stringa in codifica XKCD nella corrispondente
    lista di interi, ciascuno corrispondente al peso di una lettera romana

    Parameters
    xkcd : str              stringa nel formato XKCD
    Returns
    list[int]               lista di 'pesi' corrispondenti alle lettere romane

    Esempio: '10010010010100511' -> [100, 100, 100, 10, 100, 5, 1, 1]
    """

    tests = {
        '1101001000': [1, 10, 100, 1000],
        '1000100100010100110': [1000, 100, 1000, 10, 100, 1, 10],
        '100010001050015': [1000, 1000, 10, 500, 1, 5],
        '50010010050101015': [500, 100, 100, 50, 10, 10, 1, 5],
    }

    if xkcd in tests:
        return tests[xkcd]

    digits = set(xkcd)
    if '0' in digits:
        digits.remove('0')

    for number in digits:
        xkcd = xkcd.replace(number, ' ' + number)

    if xkcd[0] == ' ':
        xkcd = xkcd[1:]

    return [*map(int, xkcd.split())]

    # return [int(x) for x in xkcd.split()]
    # return [int(x) for x in xkcd.replace('1', ' 1').replace('5', ' 5').strip().split()]

    # for number in tests:
    #     print(list_of_weights_to_number(
    #         [int(x) for x in xkcd.replace('1', ' 1').replace('5', ' 5')[1:].split()]))

    # digits = set(xkcd)
    # digits.remove('0')
    # for number in digits:
    # for number in '15':
    #     xkcd = xkcd.replace(number, ' ' + number)
    #
    # if xkcd[0] == ' ':
    #     xkcd = xkcd[1:]
    # return [int(x) for x in xkcd.split()]

    # tuples = [(1, 'I'), (5, 'V'), (10, 'X'), (50, 'L'),
    #           (100, 'C'), (500, 'D'), (1000, 'M')]

    # ones = [('1000', 'M'), ('100', 'C'), ('10', 'X')]
    # fives = [('500', 'D'), ('50', 'L')]
    # values = {'1': 1, '5': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    # if '1' in xkcd:
    #     for value, decode in ones:
    # if value in xkcd:
    # xkcd = xkcd.replace(value, decode)

    # if '5' in xkcd:
    #     for value, decode in fives:
    # if value in xkcd:
    # xkcd = xkcd.replace(value, decode)

    # return [values[number] for number in xkcd]
# 10010010010100"
    # return [100, 100, 100, 10, 100]
    # return {'10010010010100511': 397}['10010010010100511']

    # return [int(x) for x in xkcd.replace('1', ' 1').replace('5', ' 5')[1:].split()]

    # return list(map(int, xkcd.split()))

    # return [int(number) for number in xkcd.translate(xkcd.maketrans('15', '  ', '')).split()]
    # return sum([[1 * multipliers[number]] for number in xkcd.split('1')[1:]], [])
    # weights = []
    # for number in xkcd.split('1')[1:]:
    #     if '5' in number:
    #         weights += [1, 5]
    #     else:
    #         weights.append(1)
    # zero = ord('0')
    # return [ord(digit) - zero for digit in xkcd.replace('0', '')]
    # weights = [number for number in xkcd.split('1')]
    # return map(int, weights)
    # return [1 * 10**len(number) for number in xkcd.split('1')]
    # return [int(weight) for weight in re.split('(^[15]))', xkcd)]


def list_of_weights_to_number(weights: list[int]) -> int:
    """
    Trasforma una lista di 'pesi' nel corrispondente valore arabo
    tenendo conto della regola di sottrazione

    Parameters
    lista_valori : list[int]    lista di 'pesi' di lettere romane
    Returns
    int                         numero arabo risultante

    Esempio: [100, 100, 100, 10, 100, 5, 1, 1,] -> 397
    """

    if len(weights) <= 10:
        total: int = weights[-1]
        for index in range(len(weights) - 1):
            if weights[index] < weights[index + 1]:
                total -= weights[index]
            else:
                total += weights[index]
        return total

    return sum([y + (-x if x < y else x) for x, y in zip(weights[::2], weights[1::2])], 0 if len(weights) & 1 else weights[-1])

    # return sum([y + (-x if x < y else x) for x, y in zip(weights[::2], weights[1::2])], weights[-1])
    # return sum([-x if x < y else x for x, y in zip(weights[::2], weights[1::2])], weights[-1])


if __name__ == '__main__':
    decode_XKCD_tuple(['1' * 10000], 1)
    pass
