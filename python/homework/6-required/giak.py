#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import images


def generate_snake(start_img: str, position: list[int, int], commands: str, out_img: str) -> int:
    nero = (0, 0, 0)
    rosso = (255, 0, 0)
    grigio = (128, 128, 128)
    arancione = (255, 128, 0)
    verde = (0, 255, 0)

    img = images.load(start_img)
    lunghezza = len(img[0])
    altezza = len(img)

    head = (position[0], position[1])
    snake = [(position[0], position[1])]

    nextPixelIndex = tuple()

    for mov in commands.split():
        # prossima casella
        nextPixelIndex, err = getNext(
            mov, head, altezza, lunghezza, snake, img)
        if(err):
            break

        # controllo cosa c'è
        nextPixel = img[nextPixelIndex[1]][nextPixelIndex[0]]
        if nextPixel == verde or nextPixel == rosso:
            # caso in cui SI PUò RINCORRERE LA CODA
            """if nextPixelIndex == snake[-1]:
                head = nextPixelIndex;
                snake.insert(0, nextPixelIndex);
                #coloro
                #img[nextPixelIndex[1]][nextPixelIndex[0]] = verde;
                #lo ritorna anche
                snake.pop()
            else:"""
            break
        elif nextPixel == nero or nextPixel == grigio:
            head = nextPixelIndex
            snake.insert(0, nextPixelIndex)
            # coloro
            img[nextPixelIndex[1]][nextPixelIndex[0]] = verde
            # lo ritorna anche
            indiceGrigio = snake.pop()
            img[indiceGrigio[1]][indiceGrigio[0]] = grigio

        elif nextPixel == arancione:
            head = nextPixelIndex
            snake.insert(0, nextPixelIndex)
            img[nextPixelIndex[1]][nextPixelIndex[0]] = verde

    images.save(img, out_img)

    return len(snake)


def controlloValore(val, massimo):
    if val >= massimo:
        return val - massimo
    elif val < 0:
        return massimo+val
    else:
        return val


def avanza(snake, img):
    # tolgo l'ex coda
    indiceGrigio = snake.pop()
    # e coloro la cella di grigio
    img[indiceGrigio[1]][indiceGrigio[0]] = (128, 128, 128)


def getNext(mov, head, altezza, lunghezza, snake, img):
    if mov == "N":
        nextPixelIndex = [head[0], controlloValore(head[1]-1, altezza)]
    elif mov == "E":
        nextPixelIndex = [controlloValore(head[0]+1, lunghezza), head[1]]
    elif mov == "S":
        nextPixelIndex = [head[0], controlloValore(head[1]+1, altezza)]
    elif mov == "W":
        nextPixelIndex = [controlloValore(head[0]-1, lunghezza), head[1]]
    elif mov == "NE":
        return obiNext(controlloValore(head[0]+1, lunghezza), controlloValore(head[1]-1, altezza), head, snake, img)
    elif mov == "SE":
        return obiNext(controlloValore(head[0]+1, lunghezza), controlloValore(head[1]+1, altezza), head, snake, img)
    elif mov == "NW":
        return obiNext(controlloValore(head[0]-1, lunghezza), controlloValore(head[1]-1, altezza), head, snake, img)
    elif mov == "SW":
        return obiNext(controlloValore(head[0]-1, lunghezza), controlloValore(head[1]+1, altezza), head, snake, img)

    # questo return lo uso solo per le transizioni sempre valide quindi l'errore sarà sempre 0
    return nextPixelIndex, 0


def obiNext(nextX, nextY, head, snake, img):
    err = 0
    # controllo se i pixel adiacenti sono nella mia lista (snake)
    if snake.count((head[0], nextY)) and snake.count((nextX, head[1])):
        # se lo sono allora metto un valore di errore
        err = 1
    # ritorno la tupla con i valori in cui voglio andare in piu se c'è stato un errore
    nextPixelIndex = nextX, nextY
    return nextPixelIndex, err
