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
2, 16, 0)

ATTENZIONE: la funzione dumbothello o qualche altra
funzione usata per la soluzione deve essere ricorsiva.

'''


# Pass possible slots
# Cache configurations
# Const "around" tuple
# Around function to get values around?
# Const x,y of table (so do it only once!)
# Python FAST deep copy (or function at least)
def play(board, player, position=None):
    width, height = len(board[0]), len(board)
    adversary = 'W' if player == 'B' else 'B'

    around = [(-1, -1), (0, -1), (1, -1), (-1, 0),
              (1, 0), (-1, 1), (0, 1), (1, 1)]
    if position:
        x, y = position

        board[y][x] = player

        for x_offset, y_offset in around:
            _x = x + x_offset  # What if i use modulo here? NOPE!
            _y = y + y_offset

            if 0 <= _x < width and 0 <= _y < height:
                if board[_y][_x] == adversary:
                    board[_y][_x] = player

    slots = []
    for y in range(height):
        for x in range(width):
            if board[y][x] == '.':
                is_placeable = False
                for x_offset, y_offset in around:
                    _x = x + x_offset
                    _y = y + y_offset

                    if 0 <= _x < width and 0 <= _y < height:
                        if board[_y][_x] == player:
                            is_placeable = True
                            break

                if is_placeable:
                    slots.append((x, y))

    if len(slots) == 0:
        return [''.join([''.join(line) for line in board])]

    results = []
    for x, y in slots:
        copy = [[_ for _ in line] for line in board]
        results.extend(play(copy, adversary, (x, y)))

    return results


def dumbothello(filename: str) -> tuple[int, int, int]:
    with open(filename) as file:
        board = [line.split() for line in file.read().strip().split('\n')]

    a, b, c = 0, 0, 0
    for board in play(board, 'W'):
        black = board.count('B')
        white = board.count('W')

        if black > white:
            a += 1
        elif white > black:
            b += 1
        else:
            c += 1

    return a, b, c


if __name__ == "__main__":
    R = dumbothello("boards/01.txt")
    print(R)
