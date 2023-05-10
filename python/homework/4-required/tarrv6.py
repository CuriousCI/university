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
    dupParole = operazione(filename)
    # lmax=len(max(dupParole, key=len))
    # portamo la lmax in giro per crearmi la stringa
    contaOccorrenze(dupParole, dizPosOcc)
    return creaStringa(dizPosOcc)


def operazione(filename):
    fileStop = filename
    dupParole = {}
    proxFile = ""

    # l'apertura dei file non segue un ciclo, mi devo salvare quindi quali file ho aperto
    while proxFile != fileStop:
        with open(filename, encoding="utf8") as f:
            # leggo la prima riga e salvo il nome del file successivo

            filename = f.readline().strip()
            proxFile = filename
            # mi prendo le successive parole e ne conto le occorrenze
            riga = f.read().split()
            for parola in riga:
                if parola not in dupParole:
                    dupParole[parola] = 1
                else:
                    dupParole[parola] += 1

    return dupParole


def contaOccorrenze(dupParole, dizPosOcc):
    # questa cosa la faccio prendendo la parola più lunga
    # for i in range(lmax):
    #     dizPosOcc[i]={}

    # #ho creato il dizionario {indice:dictOccorrenze}
    # #inserisco le occorrenze dei caratteri nella rispettiva poszione

    # for parola in dupParole:
    #     for index,char in enumerate(parola):
    #         occorrenze=dizPosOcc[index]
    #         if char not in occorrenze:
    #             occorrenze[char]=dupParole[parola]
    #         else:
    #             occorrenze[char]+=dupParole[parola]
    # si puo provare a creare un for unico
    for parola in dupParole:
        val = dupParole[parola]
        for index, char in enumerate(parola):

            if index not in dizPosOcc:
                dizPosOcc[index] = {char: val}
            else:
                occorrenze = dizPosOcc[index]
                if char not in dizPosOcc[index]:
                    occorrenze[char] = val
                else:
                    occorrenze[char] += val
    return dizPosOcc


def creaStringa(dizPosOcc):
    toRet = ""
    lDiz = len(dizPosOcc)
    # cerco in ogni poszione l'occorrenza massima
    for i in range(lDiz):
        occorrenze = dizPosOcc[i]
        maxOccForPos = max(occorrenze.values())
        listaKey = occorrenze.keys()

        for char in sorted(listaKey):
            if occorrenze[char] == maxOccForPos:
                toRet += char
                break

    return toRet

