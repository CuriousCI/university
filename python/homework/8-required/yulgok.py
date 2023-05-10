#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def adj(coordinates, width, height):
    return {(x, y): tuple((x + _x, y + _y)for _x, _y in ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))if 0 <= x + _x < width and 0 <= y + _y < height)for x, y in coordinates}


def play(board, move, empty=None, adjacent=None, cache=None):
    player, x, y = move
    opponent = 'W' if player == 'B' else 'B'
    board = list(map(list.copy, board))
    board[y][x] = player
    for _x, _y in adjacent[(x, y)]:
        if board[_y][_x] == opponent:
            board[_y][_x] = player
    configuration = ''.join(map(''.join, board))
    if configuration in cache:
        return cache[configuration]
    empty = empty.copy()
    empty.remove((x, y))
    results = []
    for x, y in empty:
        for _x, _y in adjacent[(x, y)]:
            if board[_y][_x] == player:
                results.extend(
                    play(board, (opponent, x, y), empty, adjacent, cache))
                break
    if not results:
        results = [configuration.count('B') - configuration.count('W')]
    cache[configuration] = results
    return results


def dumbothello(filename: str) -> tuple[int, int, int]:
    with open(filename) as file:
        board = [_.strip().split() for _ in file.readlines()]
    width, height = len(board[0]), len(board)
    empty = [(x, y)for y in range(height)
             for x in range(width)if board[y][x] == '.']
    adjacent = adj(empty, width, height)
    results, cache = [], {}
    for x, y in empty:
        for _x, _y in adjacent[(x, y)]:
            if board[_y][_x] == 'W':
                results.extend(
                    play(board, ('B', x, y), empty, adjacent, cache))
                break
    black = len([_ for _ in results if _ > 0])
    ties = results.count(0)
    white = len(results) - black - ties
    return black, white, ties


if __name__ == "__main__":
    R = dumbothello("boards/01.txt")
    print(R)
