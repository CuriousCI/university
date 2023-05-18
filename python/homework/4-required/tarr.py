#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Obiettivo dello homework è leggere alcune stringhe contenute in una serie di
file e generare una nuova stringa a partire da tutte le stringhe lette.
Le stringhe da leggere sono contenute in diversi file, collegati fra loro a
formare una catena chiusa. Infatti, la prima stringa di ogni file è il nome di
un altro file che appartiene alla catena: partendo da un qualsiasi file e
seguendo la catena, si ritorna sempre nel file di partenza.

Esempio: il contenuto di "A.txt" inizia con "B.txt", il file "B.txt", inizia
con "C.txt" e il file "C.txt" inizia con "A.txt", formando la catena
"A.txt"-"B.txt"-"C.txt".

Oltre alla stringa con il nome del file successivo, ogni file contiene anche
altre stringhe separate da spazi, tabulazioni o caratteri di a capo. La
funzione deve leggere tutte le stringhe presenti nei file della catena e
costruire la stringa che si ottiene concatenando i caratteri con la più alta
frequenza in ogni posizione. Ovvero, nella stringa da costruire, alla
posizione p ci sarà il carattere che ha frequenza massima nella posizione p di
ogni stringa letta dai file. Nel caso in cui ci fossero più caratteri con
la stessa frequenza, si consideri l'ordine alfabetico.
La stringa da costruire ha lunghezza pari alla
lunghezza massima delle stringhe lette dai file.

Quindi, si deve scrivere una funzione che prende in ingresso una stringa A 
che rappresenta il nome di un file e restituisce una stringa.
La funzione deve costruire la stringa secondo le indicazioni illustrate sopra
e ritornare le stringa così costruita.

Esempio: se il contenuto dei tre file A.txt, B.txt e C.txt nella directory
test01 è il seguente

test01/A.txt          test01/B.txt         test01/C.txt                                                                 
-------------------------------------------------------------------------------
test01/B.txt          test01/C.txt         test01/A.txt
house                 home                 kite                                                                       
garden                park                 hello                                                                       
kitchen               affair               portrait                                                                     
balloon                                    angel                                                                                                                                               
                                           surfing                                                               

la funzione most_frequent_chars("test01/A.txt") dovrà restituire la stringa
"hareennt".
'''


def most_frequent_chars(filename):
    dizPosOcc = dict()

    listaParole = operazione(filename)
    lmax = 0
    for parola in listaParole:
        if len(parola) > lmax:
            lmax = len(parola)
    contaOccorrenze(listaParole, dizPosOcc, lmax)

    toRet = creaStringa(dizPosOcc, lmax)
    # print(toRet)
    return toRet


def operazione(filename):
    parole = []
    openedFile = []
    proxFile = ""

    # l'apertura dei file non segue un ciclo, mi devo salvare quindi quali file ho aperto
    while proxFile not in openedFile:
        with open(filename, encoding="utf8") as f:
            # leggo la prima riga e salvo il nome del file successivo
            openedFile.append(filename)
            filename = f.readline().strip()
            proxFile = filename

            parole.extend(f.read().split())
            # mi prendo le successive parole e ne conto le occorrenze
            # for linea in f.readlines():
            #     tmpL = linea.split()
            #     for parola in tmpL:
            #         if parola != "":
            #             parole.append(parola)

    return parole


def contaOccorrenze(parole, dizPosOcc, lmax):
    # questa cosa la faccio prendendo la parola più lunga

    for i in range(lmax):
        dizPosOcc[i] = {}

    # ho creato il dizionario {indice:dictOccorrenze}
    # inserisco le occorrenze dei caratteri nella rispettiva poszione

    for parola in parole:
        for index, char in enumerate(parola):
            occorrenze = dizPosOcc[index]
            if char not in occorrenze:
                occorrenze[char] = 1
            else:
                occorrenze[char] += 1
    return dizPosOcc


def creaStringa(dizPosOcc, lmax):
    toRet = ""
    # cerco in ogni poszione l'occorrenza massima
    for i in range(lmax):
        occorrenze = dizPosOcc[i]
        maxOccForPos = max(occorrenze.values())
        listaKey = list(occorrenze.keys())

        for char in sorted(listaKey):
            if occorrenze[char] == maxOccForPos:
                toRet += char
                break

    return toRet


filename = "test03/woodchuck.txt"
# toRet=aanreeaseesable
most_frequent_chars(filename)
