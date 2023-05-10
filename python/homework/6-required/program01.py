#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Siete stati appena ingaggiati in una software house di videogiochi e
dovete renderizzare su immagine il giochino dello snake salvando
l'immagine finale del percorso dello snake e restituendo la lunghezza
dello snake.
Si implementi la funzione generate_snake che prende in ingresso un
percorso di un file immagine, che e' l'immagine di partenza
"start_img" che puo' contenere pixel di background neri, pixel di
ostacolo per lo snake di colore rosso e infine del cibo di colore
arancione. Lo snake deve essere disegnato di verde. Inoltre bisogna
disegnare in grigio la scia che lo snake lascia sul proprio
cammino. La funzione inoltre prende in ingresso una posizione iniziale
dello snake, "position" come una lista di due interi X e Y. I comandi
del giocatore su come muovere lo snake nel videogioco sono disponibili
in una stringa "commands".  La funzione deve salvare l'immagine finale
del cammino dello snake al percorso "out_img", che e' passato come
ultimo argomento di ingresso alla funzione. Inoltre la funzione deve
restituire la lunghezza dello snake al termine del gioco.

Ciascun comando in "commands" corrisponde ad un segno cardinale ed e
seguito da uno spazio. I segni cardinali possibli sono:

| NW | N | NE |
| W  |   | E  |
| SW | S | SE |

che corrispondono a movimenti dello snake di un pixel come:

| alto-sinistra  | alto  | alto-destra  |
| sinistra       |       | destra       |
| basso-sinistra | basso | basso-destra |

Lo snake si muove in base ai comandi passati e nel caso in cui
mangia del cibo si allunga di un pixel.

Lo snake puo' passare da parte a parte dell'immagine sia in
orizzontale che in verticale. Il gioco termina quando sono finiti i
comandi oppure lo snake muore. Lo snake muore quando:
- colpisce un ostacolo
- colpisce se stesso quindi non puo' passare sopra se stesso
- si incrocia in diagonale in qualsiasi modo. Ad esempio, un percorso
  1->2->3-4 come quello sotto a sinistra non e' lecito mentre quello a
  destra sotto va bene.

  NOT OK - diagonal cross        OK - not a diagonal cross
       | 4 | 2 |                    | 1 | 2 |
       | 1 | 3 |                    | 4 | 3 |

Ad esempio considerando il caso di test data/input_00.json
lo snake parte da "position": [12, 13] e riceve i comandi
 "commands": "S W S W W W S W W N N W N N N N N W N"
genera l'immagine in visibile in data/expected_end_00.png
e restituisce 5 in quanto lo snake e' lungo 5 pixels alla
fine del gioco.

NOTA: analizzate le immagini per avere i valori esatti dei colore da usare.

NOTA: non importate o usate altre librerie
'''


import images


# | NW | N | NE |
# | W  |   | E  |
# | SW | S | SE |

def generate_snake(start_img: str, position: list[int, int], commands: str, out_img: str) -> int:
    game, (x, y) = images.load(start_img), position
    width, height = len(game[0]), len(game)
    snake = [(x, y)]

    directions = {
        'N': (0, -1, None),
        'S': (0, 1, None),
        'W': (-1, 0, None),
        'E': (1, 0, None),
        'NW': (-1, -1, (0, -1, -1, 0)),
        'NE': (1, -1, (0, -1, 1, 0)),
        'SW': (-1, 1, (0, 1, -1, 0)),
        'SE': (1, 1, (0, 1, 1, 0)),
    }

    for command in commands.split():
        off_x, off_y, adj = directions[command]
        xm, ym = x, y

        x += off_x
        y += off_y
        x %= width
        y %= height

        if adj:
            x1, y1, x2, y2 = adj
            x1 += xm
            x2 += xm
            y1 += ym
            y2 += ym
            x1 %= width
            y1 %= height
            x2 %= width
            y2 %= height
            if game[y1][x1] == (0, 255, 0) and game[y2][x2] == (0, 255, 0):
                break

        t = snake[-1]
        if game[y][x] == (255, 0, 0):
            break
        if game[y][x] == (0, 255, 0):
            break

        if game[y][x] == (255, 128, 0):
            game[y][x] = (0, 255, 0)
            snake = [(x, y)] + snake
        else:
            tx, ty = snake.pop()
            game[ty][tx] = (128, 128, 128)
            game[y][x] = (0, 255, 0)
            snake = [(x, y)] + snake

    images.save(game, out_img)
    return len(snake)


if __name__ == '__main__':
    length = generate_snake('./data/input_04.png', [19, 35], 'S S S S W W W W N N N N N N E E E E E E E N E S S S E E E E S E S E S E S E S E N N N N N N N E N E E N E N N E N E N E N E N E N N W N W N W N W W W N W N W N W N W W W N N N N E N N E N E E E E NE NE NE NE S NW SW NE NE S SE S E W S W N E NW SE S NW NW NE SE NE S S E SW W NE NE S W NW SE S S SE NE N SW SW NW NW S S N SE SW E SE SW NW NW SW SW NE W W N SE SW S S SW S SW S S S W S E N NW NW SW S NE S SW SE NE S NW W NE W N S S SW NE SW NE SW SW NE W SW SE E W N SW W NE SE SE S W SE NW NW N E NE SW NW SW W NE NW NW NE S N E NE NE N N E E S NW SW NW E NW NE S E SW N W NE S NW NE N N N N NW SW S SW NW SW SW W NW SW SW E SE W W W NE SE SE S E S SE E W NW SE NE S SW E NW NW S SE S N W NE NW SW S E S E S NW SW S E S NW N SW N W W NE E E N N E E S W NE SE NW E SW S SW N W S S NE NW SW NE NE N W S SE SE S SE S W N S N N NW NW NW S SE S S S SW E W NE NE NW SW W N NW W NW W S N N NE NE S S W SW S N E S NW SW N', './output/output_end_04.png')

    # print(length)
