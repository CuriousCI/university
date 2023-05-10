#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import images


def generate_snake(start_img: str, position: list[int, int], commands: str, out_img: str) -> int:
    SNAKE, OBSTACLE, FOOD, TRAIL = (
        (0, 255, 0), (255, 0, 0), (255, 128, 0), (128, 128, 128)
    )

    game = images.load(start_img)
    width, height, (x, y) = len(game[0]), len(game), position
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

    for off_x, off_y, adj in map(directions.get, commands.split()):
        if adj:
            x1, y1, x2, y2 = adj
            x1 = (x + x1) % width
            x2 = (x + x2) % width
            y1 = (y + y1) % height
            y2 = (y + y2) % height

            if game[y1][x1] == SNAKE and game[y2][x2] == SNAKE:
                break

        x, y = (x + off_x) % width, (y + off_y) % height

        if game[y][x] in (OBSTACLE, SNAKE):
            break

        if game[y][x] != FOOD:
            _x, _y = snake.pop()
            game[_y][_x] = TRAIL

        snake.insert(0, (x, y))
        game[y][x] = SNAKE

    images.save(game, out_img)
    return len(snake)


if __name__ == '__main__':
    pass
