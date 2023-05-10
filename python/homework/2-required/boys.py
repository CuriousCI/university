#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 22:16:42 2022

@author: ivanopiredda90
"""

def decode_XKCD_tuple(xkcd,k):
    assert 0<=k<=len(xkcd), 'k errato'  #controllo che k sia plausibile
    lista=[]                            #creo una lista vuota
    for x in xkcd:                      #scandisco ogni lista data xkcd
        lista.append(decode_value(x))   #uso la funzione decode_value su ogni elemento e lo aggiungo alla lista
    int=sorted(lista,reverse=True)      #ordino la mia lista in ordine decrescente
    return int [:k]                     #torno i primi k valori della lista ordinata

    
def decode_value (xkcd):
    a=xkcd_to_list_of_weights(xkcd)  #uso la funzione xkcd_to_list_of_weights sulla stringa xkcd
    b= list_of_weights_to_number(a)  #uso la funzione list_of_weights_to_number sul risultato precedente
    return b                         #torno il risultato                         


def xkcd_to_list_of_weights(xkcd):   
    list=[]                     #creo una lista vuota
    a=xkcd.replace('1',' 1')    #sostituisco alla stringa xkcd data tutti i valori 1 con ' 1' (spazio e 1)
    s=a.replace('5',' 5')       #sostituisco alla stringa ottenuta tutti i valori 5 con ' 5' (spazio e 5)
    d= s.split()                #ora divido con split la stringa risultante
    for i in d:                 #scandisco quest'ultima stringa tutti i valori
        list.append (int(i))    #aggiungo alla mia lista ogni singolo elemento trasformato in intero
    return list                 #torno la lista finale di interi


def list_of_weights_to_number (lista):
    int = 0                     #creo una lista vuota
    n=1                         #imposto punto di partenza 'n'
    for x in lista[:-1]:        #scandisco gli elementi della lista uno ad uno, fino al penultimo valore compreso, escludendo di fatto solo l'ultimo valore
        if n==len(lista):       #se n è uguale alla lunghezza della lista
            break               #esco dall'iterazione con un break
        if x >= lista[n]:       #se l'elemento è maggiore o uguale al valore dell'elemento successivo in posizione 'n'
            int+= x             #aggiungo l'elemento alla mia lista
            n+=1                #ed aumento il valore di 'n' di 1, in modo che sia sempre il successore dell'elemento che sto considerando
        else:                   #altrimenti
            int -= x            #sottraggo l'elemento alla mia lista
            n+=1                #e proseguo aumentando 'n' di 1
    int+=lista[-1]              #alla fine aggiungo alla mia lista l'ultimo valore presente nella lista iniziale, che inizialmente avevo lasciato fuori dall'iterazione
    return int                  #torno l'intero risultante

