#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_adjacent(coordinates, width, height):
    return {
        (x, y): [
            (x + _x, y + _y)
            for _x, _y in (
                (-1, -1), (0, -1), (1, -1),
                (-1, 0), (1, 0),
                (-1, 1), (0, 1), (1, 1)
            )
            if 0 <= x + _x < width and 0 <= y + _y < height
        ]
        for x, y in coordinates
    }


def valid_moves(board, opponent, empty_positions, adjacent):
    moves = []

    for x, y in empty_positions:
        for _x, _y in adjacent[(x, y)]:
            if board[_y][_x] == opponent:
                moves.append((x, y))
                break

    return moves


def play(board, move, empty_positions=None, adjacent=None, cache=None):
    player, x, y = move
    opponent = 'W' if player == 'B' else 'B'

    board = list(map(list.copy, board))

    board[y][x] = player
    for _x, _y in adjacent[(x, y)]:
        if board[_y][_x] == opponent:
            board[_y][_x] = player

    b = ''.join([''.join(_) for _ in board])
    configuration = player, b

    if configuration in cache:
        return cache[configuration]

    squares = empty_positions.copy()
    squares.remove((x, y))

    results = []
    for x, y in squares:
        for _x, _y in adjacent[(x, y)]:
            if board[_y][_x] == player:
                results.extend(play(
                    board,
                    (opponent, x, y),
                    squares,
                    adjacent,
                    cache
                ))
                break

    if not results:
        results.append((b.count('B'), b.count('W')))

    cache[configuration] = results
    return results


def dumbothello(filename: str) -> tuple[int, int, int]:
    with open(filename) as file:
        board = [_.split() for _ in file.read().strip().split('\n')]

    width, height = len(board[0]), len(board)

    empty_positions = set(
        (x, y)
        for y in range(height)
        for x in range(width)
        if board[y][x] == '.'
    )

    adjacent = get_adjacent(empty_positions, width, height)

    results, cache = [], {}
    for x, y in valid_moves(board, 'W', empty_positions, adjacent):
        results.extend(play(
            board,
            ('B', x, y),
            empty_positions,
            adjacent,
            cache
        ))

    a, b, c = 0, 0, 0
    for black, white in results:
        if black > white:
            a += 1
        elif white > black:
            b += 1
        else:
            c += 1

    return a, b, c


if __name__ == "__main__":
    R = dumbothello("boards/01.txt")
    print(R)
