#!/usr/bin/env python3
# -- coding: utf-8 --


def adj(positions, width, height):
    return {
        (x, y): [
            (x + _x, y + _y)
            for _x, _y in ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))
            if 0 <= x + _x < width and 0 <= y + _y < height
        ] for x, y in positions
    }


def play(board, player, opponent, empty, adjacent, cache):
    configuration = ''.join(map(''.join, board))

    if configuration in cache:
        return cache[configuration]

    outcomes = []

    for x, y in empty:
        position = (x, y)
        adj = adjacent[position]
        for x_, y_ in adj:
            if board[y_][x_] == opponent:
                b = list(map(list.copy, board))

                e = empty.copy()
                e.remove(position)

                b[y][x] = player
                for _x, _y in adj:
                    if b[_y][_x] == opponent:
                        b[_y][_x] = player

                outcomes.extend(play(b, opponent, player, e, adjacent, cache))
                break

    if not outcomes:
        outcomes = [configuration.count('B') - configuration.count('W')]

    cache[configuration] = outcomes
    return outcomes


def dumbothello(filename: str) -> tuple[int, int, int]:
    with open(filename) as file:
        board = list(map(str.split, file))

    empty = [
        (x, y)
        for y, row in enumerate(board)
        for x, square in enumerate(row)
        if square == '.'
    ]

    adjacent = adj(empty, len(board[0]), len(board))
    cache = {}

    black, white, ties = 0, 0, 0
    for result in play(board, 'B', 'W', empty, adjacent, cache):
        if not result:
            ties += 1
        elif result > 0:
            black += 1
        else:
            white += 1

    return black, white, ties


if __name__ == "__main__":
    R = dumbothello("boards/01.txt")
    print(R)
