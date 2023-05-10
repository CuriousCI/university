#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# [ ] Cache configurations
# [ ] Cache possible_moves?

def adjacent(positions, width, height):
    return {
        (x, y): [
            (_x + x, _y + y)
            for _x, _y in (
                (-1, -1), (0, -1), (1, -1),
                (-1, 0), (1, 0),
                (-1, 1), (0, 1), (1, 1)
            )
            if 0 <= _x + x < width and 0 <= _y + y < height
        ]
        for x, y in positions
    }


def possible_moves(board, empty_positions, adjacent, player):
    moves = []

    for x, y in empty_positions:
        for _x, _y in adjacent[(x, y)]:
            if board[_y][_x] == player:
                moves.append((x, y))
                break

    return moves


def play(board, player, position=None, empty_positions=None, adjacent=None):
    adversary = 'W' if player == 'B' else 'B'

    empty_positions = empty_positions.copy()
    if position:
        x, y = position
        board[y][x] = player
        empty_positions.remove((x, y))
        for _x, _y in adjacent[(x, y)]:
            if board[_y][_x] == adversary:
                board[_y][_x] = player

    moves = possible_moves(board, empty_positions, adjacent, player)

    if not moves:
        return [''.join([''.join(line) for line in board])]

    results = []
    for x, y in moves:
        results.extend(play(
            list(map(list.copy, board)),
            adversary,
            (x, y),
            empty_positions=empty_positions,
            adjacent=adjacent
        ))

    return results


def dumbothello(filename: str) -> tuple[int, int, int]:
    with open(filename) as file:
        board = [line.split() for line in file.read().strip().split('\n')]

    width, height = len(board[0]), len(board)

    empty_positions = set([
        (x, y)
        for y in range(height)
        for x in range(width)
        if board[y][x] == '.'
    ])

    results = play(
        board,
        'W',
        empty_positions=empty_positions,
        adjacent=adjacent(empty_positions, width, height)
    )

    a, b, c = 0, 0, 0
    for board in results:
        black, white = board.count('B'), board.count('W')

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
