#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import images


def generate_snake(start_img: str, position: list[int, int], commands: str, out_img: str) -> int:
    SNAKE = (0, 255, 0)
    TRAIL = (128, 128, 128)
    FOOD = (255, 128, 0)
    OBSTACLE = (255, 0, 0)

    game = images.load(start_img)
    x, y = position
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

    for off_x, off_y, adj in map(directions.get, commands.split()):
        if adj:
            x1, y1, x2, y2 = map(sum, zip(adj, (x, y, x, y)))
            if game[y1 % height][x1 % width] == SNAKE and game[y2 % height][x2 % width] == SNAKE:
                break

        x = (x + off_x) % width
        y = (y + off_y) % height

        if game[y][x] in (OBSTACLE, SNAKE):
            break

        if game[y][x] != FOOD:
            _x, _y = snake.pop()
            game[_y][_x] = TRAIL

        game[y][x] = SNAKE
        snake.insert(0, (x, y))

    images.save(game, out_img)
    return len(snake)


if __name__ == '__main__':
    length = generate_snake('./data/input_05.png', [19, 35], 'S S S S W W W W N N N N N N E E E E E E E N E S S S E E E E S E S E S E S E S E N N N N N N N E N E E N E N N E N E N E N E N E N N W N W N W N W W W N W N W N W N W W W N N N N E N N E N E E E E NE NE NE NE S NW SW NE NE S SE S E W S W N E NW SE S NW NW NE SE NE S S E SW W NE NE S W NW SE S S SE NE N SW SW NW NW S S N SE SW E SE SW NW NW SW SW NE W W N SE SW S S SW S SW S S S W S E N NW NW SW S NE S SW SE NE S NW W NE W N S S SW NE SW NE SW SW NE W SW SE E W N SW W NE SE SE S W SE NW NW N E NE SW NW SW W NE NW NW NE S N E NE NE N N E E S NW SW NW E NW NE S E SW N W NE S NW NE N N N N NW SW S SW NW SW SW W NW SW SW E SE W W W NE SE SE S E S SE E W NW SE NE S SW E NW NW S SE S N W NE NW SW S E S E S NW SW S E S NW N SW N W W NE E E N N E E S W NE SE NW E SW S SW N W S S NE NW SW NE NE N W S SE SE S SE S W N S N N NW NW NW S SE S S S SW E W NE NE NW SW W N NW W NW W S N N NE NE S S W SW S N E S NW SW N', './output/output_end_05.png')

    pass
