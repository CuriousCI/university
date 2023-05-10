#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# [x] Pass possible slots
# [ ] Cache configurations
# [ ] Const "around" tuple
# [x] Around function to get values around?
# [x] Const x,y of table (so do it only once!) (I already do it only once!)
# [ ] Python FAST deep copy (or function at least)
# Adjacent dict!!!

def generate_adjacent(x, y, width, height, board=None):
    around = ((-1, -1), (0, -1), (1, -1), (-1, 0),
              (1, 0), (-1, 1), (0, 1), (1, 1))

    # result = []
    for x_offset, y_offset in around:
        _x = x + x_offset
        _y = y + y_offset

        if 0 <= _x < width and 0 <= _y < height:
            if not board:
                yield _x, _y
            else:
                yield board[_y][_x]

# for _x, _y in generate_adjacent(x, y, width, height):
# player in generate_adjacent(x, y, width, height, board=board):


def play(board, player, position=None, slots=None):
    width, height = len(board[0]), len(board)
    adversary = 'W' if player == 'B' else 'B'
    around = [(-1, -1), (0, -1), (1, -1), (-1, 0),
              (1, 0), (-1, 1), (0, 1), (1, 1)]

    if position:
        x, y = position
        board[y][x] = player
        for x_offset, y_offset in around:
            _x = x + x_offset
            _y = y + y_offset

            if 0 <= _x < width and 0 <= _y < height:
                if board[_y][_x] == adversary:
                    board[_y][_x] = player

    s = []
    for x, y in slots:
        if board[y][x] == '.':
            for x_offset, y_offset in around:
                _x = x + x_offset
                _y = y + y_offset

                if 0 <= _x < width and 0 <= _y < height:
                    if board[_y][_x] == player:
                        s.append((x, y))
                        break

    if len(s) == 0:
        return [''.join([''.join(line) for line in board])]

    results = []
    for x, y in s:
        sl = slots.copy()
        if position:
            sl.remove((position[0], position[1]))
        results.extend(play(
            list(map(list.copy, board)),
            adversary, (x, y),
            slots=sl
        ))

    return results


def dumbothello(filename: str) -> tuple[int, int, int]:
    with open(filename) as file:
        board = [line.split() for line in file.read().strip().split('\n')]

    width, height = len(board[0]), len(board)

    slots = set()
    for y in range(height):
        for x in range(width):
            if board[y][x] == '.':
                slots.add((x, y))

    a, b, c = 0, 0, 0
    for board in play(board, 'W', slots=slots):
        black = board.count('B')
        white = board.count('W')

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
