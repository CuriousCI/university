#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Othello, o Reversi (https://en.wikipedia.org/wiki/Reversi), è un gioco da tavolo
giocato da due giocatori su una scacchiera 8x8. Pur avendo regole
relativamente semplici, Othello è un gioco di notevole profondità strategica.
In questo esercizio bisognerà simulare una versione semplificata di othello,
chiamata Dumbothello, in cui un giocatore cattura le pedine dell'avversario in
prossimità della propria pedina appena giocata.
Ecco le regole di Dumbothello:
- ogni giocatore ha un colore associato: bianco, nero;
- il giocatore con il nero è sempre il primo a giocare;
- a turno, ogni giocatore deve mettere una pedina del suo colore in modo tale
  da catturare una o più pedine avversarie;
- catturare una o più pedine avversarie vuol dire che la pedina giocata dal
  giocatore trasforma nel colore del giocatore tutte le pedine avversarie
  direttamente adiacenti, in una qualunque direzione orizzontale, verticale o diagonale;
- dopo aver giocato la propria pedina, le pedine avversarie catturate cambiano
  tutte colore e diventano dello stesso colore del giocatore che ha appena giocato;
- quando il giocatore di turno non può aggiungere ulteriori pedine in gioco,
  la partita termina. Vince il giocatore che ha più pedine sulla scacchiera
  oppure avviene un pareggio se il numero di pedine dei due giocatori è uguale;
- il giocatore di turno non può aggiungere ulteriori pedine se non ha modo di
  catturare nessuna pedina avversaria con nessuna mossa, oppure non ci sono
  più caselle libere sulla scacchiera.

Si deve scrivere una funzione dumbothello(filename) che legga da un file di testo
indicato dalla stringa filename una configurazione della scacchiera e,
seguendo le regole di Dumbothello, generi ricorsivamente l'albero di gioco completo
delle possibili evoluzioni della partita, in modo tale che ogni foglia dell'albero
sia una configurazione da cui non sia più possibile effettuare alcuna mossa.

La configurazione inziale della scacchiera nel file è rappresentata riga per
riga nel file. Una lettera "B" identifica una pedina del nero, una "W" una
pedina del bianco e il carattere "." una casella vuota. Le lettere sono
separate da uno o più caratteri di spaziatura.

In particolare, la funzione dumbothello restituirà una tripla (a, b, c), in cui:
- a è il numero totale di evoluzioni che terminano con una vittoria del nero;
- b è il numero totale di evoluzioni che terminano con una vittoria del bianco;
- c è il numero totale di evoluzioni che terminano con un pari.

Ad esempio, dato in input un file di testo contenente la scacchiera:
. . W W
. . B B
W W W B
W B B W

La funzione ritornerà la tripla:
(2, 16, 0)

ATTENZIONE: la funzione dumbothello o qualche altra 
funzione usata per la soluzione deve essere ricorsiva.

'''
# OK
# leggo la matrice in input


def getMatrice(filename):
    matrice = []
    with open(filename, 'r', encoding='utf-8') as f:
        vuoto = []
        for y, line in enumerate(f):
            array = []
            for x, lettera in enumerate(line.split()):
                array.append(lettera)
                if lettera == ".":
                    vuoto.append((x, y))
            matrice.append(array)
    return matrice, len(matrice), len(matrice[0]), vuoto

# TODO controllare se speculare
# TODO Controllo vittoria non ogni volta


class Bord:

    def __init__(self, matrice, altezza, larghezza, spazi, turno="B", stato="", nextBords=None):
        # valore
        self.spazi = spazi
        self.matrice = matrice
        self.larghezza = larghezza
        self.altezza = altezza
        self.turno = turno
        self.stato = stato
        self.nextBords = nextBords

    def nextMoves(self):
        prova = 0
        for x, y in self.spazi:
            if self.checkValidita(x, y, self.turno):
                self.nuovaMatrice(x, y, self.turno)
                prova += 1
        return prova

    def checkValidita(self, X, Y, turno):
        nextTurno = "W" if turno == "B" else "B"
        for y in range(max(Y-1, 0), min(Y+2, self.altezza)):
            for x in range(max(X-1, 0), min(X+2, self.larghezza)):
                if self.matrice[y][x] == nextTurno:
                    return True
        return False

    def nuovaMatrice(self, X, Y, turno):
        new = [i.copy() for i in self.matrice]
        new[Y][X] = turno
        nuoviSpazi = self.spazi.copy()
        nuoviSpazi.remove((X, Y))
        nextTurno = "W" if turno == "B" else "B"

        for y in range(max(Y-1, 0), min(Y+2, self.altezza)):
            for x in range(max(X-1, 0), min(X+2, self.larghezza)):
                if new[y][x] == nextTurno:
                    new[y][x] = turno

        if self.nextBords == None:
            self.nextBords = [
                Bord(new, self.altezza, self.larghezza, nuoviSpazi, turno=nextTurno)]
        else:
            self.nextBords.append(
                Bord(new, self.altezza, self.larghezza, nuoviSpazi, turno=nextTurno))

    # possibile efficentarlo
    def calcoloVincitore(self):
        text = "".join(["".join(line) for line in self.matrice])
        b = text.count("B")
        w = text.count("W")
        """
        for righe in self.matrice:
            for cella in righe:
                if cella == "B":
                    b+=1;
                elif cella == "W":
                    w +=1;
        """
        """
        if b == w:
            self.stato = "P"
        elif b>w:
            self.stato = "P"
        else:
            self.stato = "w""
        """
        self.stato = "P" if b == w else ("B" if b > w else "W")
        return self.stato

    def gioca(self):
        out = 0, 0, 0

        if self.nextMoves() == 0:
            self.calcoloVincitore()
            return (0, 0, 1) if self.stato == "P" else ((1, 0, 0) if self.stato == "B" else (0, 1, 0))
        else:
            for i in self.nextBords:
                a = i.gioca()
                out = out[0] + a[0], out[1] + a[1], out[2] + a[2]
            return out


"""        
    def show(self):
        for i in self.matrice:
            print(i)
"""


def dumbothello(filename: str) -> tuple[int, int, int]:
    matrice, altezza, larghezza, spazi = getMatrice(filename)
    radice = Bord(matrice, altezza, larghezza, spazi)
    return radice.gioca()


if __name__ == "__main__":
    R = dumbothello("boards/01.txt")
    print(R)

