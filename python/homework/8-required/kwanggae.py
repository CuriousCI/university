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


def play(board, player, opponent, empty, adjacent, positions):
    position = ''.join(map(''.join, board))

    if position in positions:
        return positions[position]

    outcomes = []

    for x, y in empty:
        pos = x, y
        adj = adjacent[pos]

        b = list(map(list.copy, board))
        is_valid = False

        b[y][x] = player
        for _x, _y in adj:
            if b[_y][_x] == opponent:
                b[_y][_x] = player
                is_valid = True

        if is_valid:
            e = empty.copy()
            e.remove(pos)

            outcomes.extend(play(b, opponent, player, e, adjacent, positions))

    if not outcomes:
        outcomes = [position.count('B') - position.count('W')]

    positions[position] = outcomes
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

    black, white, ties = 0, 0, 0
    for result in play(board, 'B', 'W', empty, adjacent, {}):
        if not result:
            ties += 1
        elif result > 0:
            black += 1
        else:
            white += 1

    return black, white, ties
