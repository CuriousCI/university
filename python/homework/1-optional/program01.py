# -*- coding: utf-8 -*-

'''
Abbiamo una stringa int_seq contenente una sequenza di interi non-negativi
    separati da virgole ed un intero positivo subtotal.

Progettare una funzione ex1(int_seq, subtotal) che
    riceve come argomenti la stringa int_seq e l'intero subtotal e
    restituisce il numero di sottostringhe di int_seq
    la somma dei cui valori è subtotal.

Ad esempio, per int_seq='3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2' e subtotal=9,
    la funzione deve restituire 7.

Infatti:
'3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2'
 _'0,4,0,3,1,0,1'_______________
 _'0,4,0,3,1,0,1,0'_____________
____'4,0,3,1,0,1'_______________
 ___'4,0,3,1,0,1,0'_____________
____________________'0,0,5,0,4'_
______________________'0,5,0,4'_
 _______________________'5,0,4'_

NOTA: è VIETATO usare/importare ogni altra libreria a parte quelle già presenti

NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test (sulla VM)

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8
    (ad esempio editatelo dentro Spyder)
'''


def ex1(int_seq: str, subtotal: int) -> int:
    numbers = list(map(int, int_seq.split(',')))

    valid_substrings, tail, segment, zeros = 0, 0, 0, 0

    for number in numbers:
        segment += number

        while segment > subtotal:
            if zeros:
                tail += zeros
                zeros = 0
            segment -= numbers[tail]
            tail += 1

        if segment == subtotal:
            if numbers[tail]:
                zeros = 0
            elif not zeros:
                leading_zeros = tail + 1
                while not numbers[leading_zeros]:
                    leading_zeros += 1
                zeros = leading_zeros - tail
            valid_substrings += 1 + zeros

    return valid_substrings


if __name__ == '__main__':
    pass
