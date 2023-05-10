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

    return sorted(map(decode_value, xkcd_values), reverse=True)[:k]


def decode_value(xkcd: str) -> int:
    """
    Decodifica un valore nel formato XKCD e torna l'intero corrispondente.

    Parameters
    xkcd : str                  stringa nel formato XKCD
    Returns
    int                         intero corrispondente

    Esempio: '10010010010100511' -> 397
    """

    # if xkcd in store:
    #     return store[xkcd]
    #

    # weigth, previous, total = "", 0, 0
    #
    # for digit in xkcd[::-1]:
    #     weigth = digit + weigth
    #
    #     if digit != "0":
    #         weigth = int(weigth)
    #         if previous > weigth:
    #             total -= weigth
    #         else:
    #             total += weigth
    #         previous = weigth
    #         weigth = ""

    # store[xkcd] = total

    # return total

    # if xkcd in store:
    #     return store[xkcd]

    # total = list_of_weights_to_number(xkcd_to_list_of_weights(xkcd))
    # store[xkcd] = total
    # return total
    return list_of_weights_to_number(xkcd_to_list_of_weights(xkcd))


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
    # keys = (
    #     ("1000", "a"),
    #     ("100", "b"),
    #     ("10", "c"),
    #     ("1", "d"),
    #     ("500", "e"),
    #     ("50", "f"),
    #     ("5", "g"),
    # )
    # weigths = {"a": 1000, "b": 100, "c": 10, "d": 1, "e": 500, "f": 50, "g": 5}
    #
    # for weigth, key in keys:
    #     xkcd = xkcd.replace(weigth, key)
    #
    # return [weigths[key] for key in xkcd]

    weigth, weigths = "", []

    for digit in xkcd[::-1]:
        weigth = digit + weigth

        if digit != "0":
            weigths.append(weigth)
            weigth = ""

    return list(map(int, weigths))[::-1]
    # weigths = list(map(int, weigths))
    # weigths.reverse()
    # return weigths

    # keys = (
    #     ("000", "a"),
    #     ("00", "b"),
    #     ("0", "c"),
    # )
    # weigths = {"a": 1000, "b": 100, "c": 10, "1": 1, "5": 1}
    #
    # for weigth, key in keys:
    #     xkcd = xkcd.replace(weigth, key)
    #
    # result = [int(d) * weigths[z] for d, z in zip(xkcd, xkcd[1:]) if d in "15"]
    # if xkcd[-1] in "15":
    #     result.append(int(xkcd[-1]))
    #
    # return result

    # keys = [
    #     ("000", "a"),
    #     ("00", "b"),
    #     ("0", "c"),
    #     ("11", "1d1"),
    #     ("15", "1d5"),
    #     ("51", "5d1"),
    #     ("55", "5d5"),
    # ]
    # weigths = {"a": 1000, "b": 100, "c": 10, "d": 1}
    #
    # for weigth, key in keys:
    #     xkcd = xkcd.replace(weigth, key)
    #
    # result = [int(d) * weigths[z] for d, z in zip(xkcd[::2], xkcd[1::2])]
    # if xkcd[-1] in "15":
    #     result += [int(xkcd[-1])]
    #
    # return result

    # result = []
    # temp = 1
    # for digit in xkcd:
    #     if digit in weigths:
    #         temp = weigths[digit]
    #     else:
    #         result.append(int(digit) * temp)
    #         temp = 1

    # return [weigths[key] for key in xkcd]
    # return result


def list_of_weights_to_number(weigths: list[int]) -> int:
    """
    Trasforma una lista di 'pesi' nel corrispondente valore arabo
    tenendo conto della regola di sottrazione

    Parameters
    lista_valori : list[int]    lista di 'pesi' di lettere romane
    Returns
    int                         numero arabo risultante

    Esempio: [100, 100, 100, 10, 100, 5, 1, 1,] -> 397
    """

    return sum([-x if x < y else x for x, y in zip(weigths, weigths[1:])]) + weigths[-1]


if __name__ == "__main__":
    pass
