# -*- coding: utf-8 -*-
'''
In un file di testo e' riportata una sequenza binaria S. Siamo interessati
    alla  frequenza delle sottosequenze di S(la frequenza di una sottosequenza
    di S e'  il numero di volte che la sottosequenza occorre in S). Si consideri
    ad esempio il file di testo f1.txt contenente la sequenza

    01010010010001000111101100001010011001111000010010011110010000000

    la sottosequenza '00' ha frequenza 23 mentre la sottosequenza '1000' ha
    frequenza 5. Notare che la sottosequenza e' separata su tre righe nel file.

Dati gli interi a e b, con a<=b, siamo interessati a contare le frequenze delle
    sottosequenze si S che presentano una lunghezza tra a e b. Dato l'intero
    n vogliamo listare le al piu' n frequenze massime ciascuna con le
    corrispondenti sottosequenze. Nel caso ci siano meno di n distinte
    frequenze con lunghezza tra a e b, l'output avra' meno di n elementi.

Progettare la funzione ex1(ftesto, a, b, n) che prende come parametri:
    - ftesto: l'indirizzo del file di testo in cui e' registrata la sequenza
      binaria in una o piu' righe consecutive;
    - a,b: i due interi a e b con a<=b che indicano l'intervallo delle
      lunghezze delle sottosequenze  di cui contare le frequenze;
    - n: l'intero che indica il numero di frequenze massime cui siamo
      interessati;
e restituisce una lista di tuple.

Ciascuna tupla della lista ha come prima coordinata una frequenza e come
    seconda coordinata la lista delle sottosequenze che hanno quella frequenza.
    La lista deve contenere solo le tuple con le prime n frequenze massime e, in
    caso ci siano meno di n frequenze distinte, conterra' tutte le tuple con
    frequenze distinte. La lista e' ordinata in ordine lessicografico rispetto
    alla prima coordinata delle tuple e in ciascuna tupla la lista presente
    nella seconda coordinata e' ordinata lessicograficamente.

Ad esempio, ex1('ft1.txt', 2, 4, 20) restituisce la lista:
    [ (4, ['0001', '0011', '1100' ]),
      (5, ['011', 1000', '110' ]),
      (6, ['0000', '111']),
      (7, ['0010','1001' ]),
      (8, ['0100']),
      (10,['010']),
      (11,['000', '001', '11']),
      (12,['100']),
      (15,['01','10']),
      (23,['00'])
    ]

NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test.

ATTENZIONE: quando caricate il file, assicuratevi che sia nella codifica UTF8
    (ad esempio editatelo dentro Spyder).

'''


def ex1(ftesto, a, b, n):
    with open(ftesto) as file:
        sequence = file.read().replace('\n', '')

    frequencies = {}
    for length in range(a, b+1):
        for index in range(len(sequence) - length + 1):
            subsequence = sequence[index:index+length]
            frequencies[subsequence] = frequencies.get(subsequence, 0) + 1

    result = {frequency: [] for frequency in set(frequencies.values())}
    for subsequence, frequency in sorted(frequencies.items()):
        result[frequency].append(subsequence)

    return sorted(result.items())[max(len(result) - n, 0):]


if __name__ == '__main__':
    for x, y in ex1('ft1.txt', 2, 4, 20):
        print((x, y))
    pass
