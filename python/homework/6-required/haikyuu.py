#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import images


def generate_snake(start_img: str, position: list[int, int], commands: str, out_img: str) -> int:
    SNAKE, OBSTACLE, FOOD, TRAIL = (
        (0, 255, 0), (255, 0, 0), (255, 128, 0), (128, 128, 128)
    )

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

    # for command in commands.split():
    for command in map(directions.get, commands.split()):
        # off_x, off_y, adj = directions[command]
        off_x, off_y, adj = command

        if adj:
            x1, y1, x2, y2 = adj
            x1 = (x + x1) % width
            x2 = (x + x2) % width
            y1 = (y + y1) % height
            y2 = (y + y2) % height

            if game[y1][x1] == SNAKE and game[y2][x2] == SNAKE:
                break

        x = (x + off_x) % width
        y = (y + off_y) % height

        if game[y][x] in (OBSTACLE, SNAKE):
            break

        if game[y][x] != FOOD:
            tx, ty = snake.pop()
            game[ty][tx] = TRAIL

        game[y][x] = SNAKE
        snake.insert(0, (x, y))

    images.save(game, out_img)
    return len(snake)

# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# import images
#
#
# def generate_snake(start_img: str, position: list[int, int], commands: str, out_img: str) -> int:
#     SNAKE, OBSTACLE, FOOD, TRAIL = (
#         (0, 255, 0), (255, 0, 0), (255, 128, 0), (128, 128, 128)
#     )
#
#     game, (x, y) = images.load(start_img), position
#     width, height = len(game[0]), len(game)
#     snake = [(x, y)]
#
#     directions = {
#         'N': (0, -1, None),
#         'S': (0, 1, None),
#         'W': (-1, 0, None),
#         'E': (1, 0, None),
#         'NW': (-1, -1, (0, -1, -1, 0)),
#         'NE': (1, -1, (0, -1, 1, 0)),
#         'SW': (-1, 1, (0, 1, -1, 0)),
#         'SE': (1, 1, (0, 1, 1, 0)),
#     }
#
#     for command in map(directions.get, commands.split()):
#         off_x, off_y, adj = command
#
#         if adj:
#             x1, y1, x2, y2 = adj
#             x1 = (x + x1) % width
#             x2 = (x + x2) % width
#             y1 = (y + y1) % height
#             y2 = (y + y2) % height
#
#             if game[y1][x1] == SNAKE and game[y2][x2] == SNAKE:
#                 break
#
#         x = (x + off_x) % width
#         y = (y + off_y) % height
#
#         if game[y][x] in (OBSTACLE, SNAKE):
#             break
#
#         if game[y][x] != FOOD:
#             tx, ty = snake.pop()
#             game[ty][tx] = TRAIL
#
#         game[y][x] = SNAKE
#         snake.insert(0, (x, y))
#
#     images.save(game, out_img)
#     return len(snake)
#
#
# if __name__ == '__main__':
#     pass
#     # print(length)
#     # for command in commands.split():
#     # off_x, off_y, adj = directions[command]
