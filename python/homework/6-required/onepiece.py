#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import images


def generate_snake(start_img: str, position: list[int, int], commands: str, out_img: str) -> int:
    offsets = {'N': (0, -1, 0), 'S': (0, 1, 0), 'W': (-1, 0, 0), 'E': (1, 0, 0),
               'NW': (-1, -1, 1), 'NE': (1, -1, 1), 'SW': (-1, 1, 1), 'SE': (1, 1, 1)}
    game, (x, y) = images.load(start_img), position
    width, height, snake = len(game[0]), len(game), [(x, y)]
    for direction in commands.split():
        (_x, _y, adjacent), __x, __y = offsets[direction], x, y
        x, y = (x + _x) % width, (y + _y) % height
        if (adjacent and game[__y][x] == (0, 255, 0) and game[y][__x] == (0, 255, 0)) or game[y][x] in ((0, 255, 0), (255, 0, 0)):
            break
        elif game[y][x] != (255, 128, 0):
            _x, _y = snake.pop()
            game[_y][_x] = (128, 128, 128)
        game[y][x] = (snake.insert(0, (x, y)), (0, 255, 0))[1]
    return (images.save(game, out_img), len(snake))[1]
