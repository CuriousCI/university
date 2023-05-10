# -*- coding: utf-8 -*-
import images


def fMapCommands(commands):
    moveMapping = {
        "NW": (-1, -1), "N": (-1, 0), "NE": (-1, 1),
        "W": (0, -1), "E": (0, 1),
        "SW": (1, -1), "S": (1, 0), "SE": (1, 1)
    }
    commands = commands.split()

    mappedComms = []
    for c in commands:
        mappedComms.append(moveMapping[c])
    return mappedComms


class Snake:
    length = 1

    def addLen(self):
        self.length += 1


class Colors:
    def __init__(self):
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.ORANGE = (255, 128, 0)
        self.GREY = (128, 128, 128)


def fSnake(img, snakePath, lenSnake, X, Y, green, grey):
    img[X][Y] = green
    snakePath.append([X, Y])
    if len(snakePath) > lenSnake:
        k = snakePath.pop(0)
        img[k[0]][k[1]] = grey


def fLoadFrames(init_img, commands, position, out_img):
    h = len(init_img)  # All Rows
    w = len(init_img[0])  # All Columns
    X = position[1]  # Row
    Y = position[0]  # Column
    c = Colors()
    s = Snake()
    snakePath = [[X, Y]]

    init_img[X][Y] = c.GREEN
    for step in commands:
        X += step[0]
        Y += step[1]

# Out of Range
        X %= h
        Y %= w

# Check Diagonal
        if sum(step) % 2 == 0:
            if init_img[X][(Y-step[1]) % w] == c.GREEN and init_img[(X-step[0]) % h][Y] == c.GREEN:
                break

# Check Red or Green
        if init_img[X][Y] == c.RED or init_img[X][Y] == c.GREEN:
            break

# Check Orange
        if init_img[X][Y] == c.ORANGE:
            s.addLen()

# Create Snake
        fSnake(init_img, snakePath, s.length, X, Y, c.GREEN, c.GREY)

    images.save(init_img, out_img)
    return s.length


def generate_snake(start_img: str, position: list[int, int],
                   commands: str, out_img: str) -> int:
    img = images.load(start_img)
    lenSnake = fLoadFrames(img, fMapCommands(commands), position, out_img)
    return lenSnake
