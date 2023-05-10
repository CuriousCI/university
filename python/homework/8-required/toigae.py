#!/usr/bin/env python3
# -- coding: utf-8 --


def adj(coordinates, width, height):
    return {
        (x, y): tuple(
            (x + _x, y + _y)
            for _x, _y in ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))
            if 0 <= x + _x < width and 0 <= y + _y < height
        ) for x, y in coordinates
    }


def play(board, player, opponent, empty, adjacent):
    outcomes = []

    for x, y in empty:
        for x_, y_ in adjacent[(x, y)]:
            if board[y_][x_] == opponent:
                b = list(map(list.copy, board))
                b[y][x] = player

                e = empty.copy()
                e.remove((x, y))

                for _x, _y in adjacent[(x, y)]:
                    if b[_y][_x] == opponent:
                        b[_y][_x] = player

                outcomes.extend(play(b, opponent, player, e, adjacent))

                break

    if not outcomes:
        outcome = ''.join(map(''.join, board))
        return [outcome.count('B') - outcome.count('W')]

    return outcomes


def dumbothello(filename: str) -> tuple[int, int, int]:
    with open(filename) as file:
        board = list(map(str.split, file.readlines()))

    width, height = len(board[0]), len(board)
    empty = [
        (x, y)
        for y in range(height)
        for x in range(width)
        if board[y][x] == '.'
    ]

    black, white, ties = 0, 0, 0
    for result in play(board, 'B', 'W', empty, adj(empty, width, height)):
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
