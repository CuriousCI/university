#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import images


def generate_snake(start_img: str, position: list[int, int],
                   commands: str, out_img: str) -> int:
    SNAKE = 0, 255, 0
    TRAIL = 128, 128, 128
    OBSTACLES = (255, 0, 0), SNAKE
    FOOD = 255, 128, 0

    offsets = {
        'N': (0, -1, False),
        'S': (0, 1, False),
        'W': (-1, 0, False),
        'E': (1, 0, False),
        'NW': (-1, -1, True),
        'NE': (1, -1, True),
        'SW': (-1, 1, True),
        'SE': (1, 1, True),
    }

    game = images.load(start_img)
    width, height, (x, y) = len(game[0]), len(game), position

    snake = [(x, y)]

    for direction in commands.split():
        offset_x, offset_y, is_diagonal = offsets[direction]
        prev_x, prev_y = x, y

        x = (x + offset_x) % width
        y = (y + offset_y) % height

        if (is_diagonal and game[prev_y][x] == SNAKE and game[y][prev_x] == SNAKE)\
                or game[y][x] in OBSTACLES:
            break

        if game[y][x] != FOOD:
            tail_x, tail_y = snake.pop()
            game[tail_y][tail_x] = TRAIL

        snake.insert(0, (x, y))
        game[y][x] = SNAKE

    images.save(game, out_img)
    return len(snake)
