#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import images


def generate_snake(start_img: str, position: list[int, int], commands: str, out_img: str) -> int:
    SNAKE = 0, 255, 0
    TRAIL = 128, 128, 128
    OBSTACLE = 255, 0, 0
    FOOD = 255, 128, 0

    offsets = {
        'N': (0, -1, None),
        'S': (0, 1, None),
        'W': (-1, 0, None),
        'E': (1, 0, None),
        'NW': (-1, -1, (-1, -1)),
        'NE': (1, -1, (1, -1)),
        'SW': (-1, 1, (-1, 1)),
        'SE': (1, 1, (1, 1)),
    }

    game = images.load(start_img)
    width, height = len(game[0]), len(game)
    x, y = position
    snake = [(x, y)]

    for direction in commands.split():
        x_offset, y_offset, adjacent = offsets[direction]

        if adjacent:
            _x, _y = adjacent
            _x = (x + _x) % width
            _y = (y + _y) % height

            if game[_y][x] == SNAKE and game[y][_x] == SNAKE:
                break

        x = (x + x_offset) % width
        y = (y + y_offset) % height

        if game[y][x] in (OBSTACLE, SNAKE):
            break

        if game[y][x] != FOOD:
            _x, _y = snake.pop()
            game[_y][_x] = TRAIL

        game[y][x] = SNAKE
        snake.insert(0, (x, y))

    images.save(game, out_img)
    return len(snake)
