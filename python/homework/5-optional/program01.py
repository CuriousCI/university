# -*- coding: utf-8 -*-
"""
Una serie di poster rettangolari sono stati affissi ad un muro.  I
   loro lati sono orizzontali e verticali. Ogni poster può essere
   parzialmente o totalmente coperto dagli altri. Chiameremo
   perimetro la lunghezza del contorno dell'unione di tutti i posters
   sul muro. Si guardi l'immagine in "posters.png" in cui i poster sulla
   parete compaiono in bianco coi bordi blu e la si confronti con l'immagine
   "posters1.png" in cui in rosso vengono evidenziati i soli
   bordi che contribuiscono al perimetro.

Vogliamo un programma che calcola il perimetro dei poster e produce
   una immagine simile a "posters1.png".

Progettare dunque una funzione
     ex1(ftesto, filepng)
   che prenda come parametri
   - ftesto, l'indirizzo di un file di testo contenente le informazioni sulla
     posizione dei poster sul muro,

   - filepng, nome del file immagine in formato PNG da produrre

   e restituisca il perimetro dei poster come numero di pixel rossi.

Il file di testo contiene tante righe quanti sono i poster,
   nell'ordine in cui sono stati affissi alla parete. In ciascuna
   riga ci sono le coordinate intere del vertice in basso a sinistra e
   del vertice in alto a destra del poster. I valori di queste
   coordinate sono dati come coppie ordinate della coordinata x
   seguita dalla coordinata y. Si veda ad esempio il file
   rettangoli_1.txt contenente le specifiche per i 7 posters in
   "posters.png".

L'immagine da salvare in filepng deve avere lo sfondo nero, altezza h
   +10 e larghezza w+10 dove h è la coordinata x massima del muro su
   cui compaiono poster e w la coordinata y massima del muro su cui
   compaiono posters. I bordi visibili dei poster sono colorati di
   rosso o di verde a seconda che appartengano al perimetro o meno.
   Notare che un pixel si trova sul perimetro (e quindi è rosso) se nel
   suo intorno (gli 8 pixel adiacenti) si trova almeno un pixel esterno
   a tutti i poster.

   Per caricare e salvare i file PNG si possono usare le funzioni load
   e save presenti nel modulo "images".

Per esempio: ex1('rettangoli_1.txt', 'test_1.png') deve costruire un file PNG
   identico a "posters1.png" e restituire il valore 1080.

NOTA: il timeout previsto per questo esercizio è di 1.5 secondi per ciascun
   test

ATTENZIONE: quando caricate il file assicuratevi che sia nella
    codifica UTF8 (ad esempio editatelo dentro Spyder)

"""

from images import save


def ex1(ftesto, filepng):
    rectangles = []

    with open(ftesto) as file:
        rectangles.extend(
            map(lambda rectangle: list(map(int, rectangle.split())), file.readlines())
        )

    width = max(rectangles, key=lambda x: x[2])[2] + 10
    height = max(rectangles, key=lambda x: x[1])[1] + 10

    BACKGROUND, POSTER, BORDER, PERIMETER = (
        (0, 0, 0),
        (255, 255, 255),
        (0, 255, 0),
        (255, 0, 0),
    )

    image = [[BACKGROUND for _ in range(width)] for _ in range(height)]

    outlines = set()
    for rectangle in rectangles:
        lb_x, lb_y, tr_x, tr_y = rectangle

        for x in range(lb_x + 1, tr_x):
            for y in range(tr_y + 1, lb_y):
                if image[y][x] == PERIMETER:
                    outlines.remove((y, x))
                image[y][x] = POSTER

        for x in range(lb_x, tr_x + 1):
            if image[lb_y][x] == POSTER:
                image[lb_y][x] = BORDER
            else:
                image[lb_y][x] = PERIMETER
                if 1 < lb_y < height - 1 and 1 < x < width - 1:
                    outlines.add((lb_y, x))

            if image[tr_y][x] == POSTER:
                image[tr_y][x] = BORDER
            else:
                image[tr_y][x] = PERIMETER
                if 1 < tr_y < height - 1 and 1 < x < width - 1:
                    outlines.add((tr_y, x))

        for y in range(tr_y, lb_y + 1):
            if image[y][tr_x] == POSTER:
                image[y][tr_x] = BORDER
            else:
                image[y][tr_x] = PERIMETER
                if 1 < y < height - 1 and 1 < tr_x < width - 1:
                    outlines.add((y, tr_x))

            if image[y][lb_x] == POSTER:
                image[y][lb_x] = BORDER
            else:
                image[y][lb_x] = PERIMETER
                if 1 < y < height - 1 and 1 < lb_x < width - 1:
                    outlines.add((y, lb_x))

    perimeter = 0
    for y, x in outlines:
        around = [
            image[y - 1][x],
            image[y + 1][x],
            image[y][x - 1],
            image[y][x + 1],
            image[y - 1][x - 1],
            image[y + 1][x + 1],
            image[y + 1][x - 1],
            image[y - 1][x + 1],
        ]

        if BACKGROUND not in around and image[y][x] != POSTER:
            image[y][x] = BORDER

    for y, x in outlines:
        if image[y][x] == PERIMETER:
            perimeter += 1

    save(image, filepng)

    return perimeter


if __name__ == "__main__":
    ex1("rectangles_1.txt", "test_1.png")
    pass
