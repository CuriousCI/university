#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def adj(coordinates, width, height):
    return {
        (x, y): tuple(
            (x + _x, y + _y)
            for _x, _y in ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))
            if 0 <= x + _x < width and 0 <= y + _y < height
        )
        for x, y in coordinates
    }


def play(board, player, move, empty, adjacent):
    opponent = 'W' if player == 'B' else 'B'
    board = list(map(list.copy, board))

    if move:
        x, y = move
        board[y][x] = player

        empty = empty.copy()
        empty.remove((x, y))

        for _x, _y in adjacent[(x, y)]:
            if board[_y][_x] == opponent:
                board[_y][_x] = player

    results = []
    for x, y in empty:
        for _x, _y in adjacent[(x, y)]:
            if board[_y][_x] == player:
                results.extend(play(board, opponent, (x, y), empty, adjacent))
                break

    if not results:
        configuration = ''.join(map(''.join, board))
        # blacks - (len(configuration) + len(empty))
        results = [configuration.count('B') - configuration.count('W')]

    return results


def dumbothello(filename: str) -> tuple[int, int, int]:
    with open(filename) as file:
        board = [_.strip().split() for _ in file.readlines()]

    width, height = len(board[0]), len(board)

    empty = [
        (x, y)
        for y in range(height)
        for x in range(width)
        if board[y][x] == '.'
    ]

    adjacent = adj(empty, width, height)
    results = play(board, 'W', None, empty, adjacent)

    black = len([_ for _ in results if _ > 0])
    ties = results.count(0)
    white = len(results) - black - ties

    return black, white, ties


if __name__ == "__main__":
    R = dumbothello("boards/01.txt")
    print(R)
