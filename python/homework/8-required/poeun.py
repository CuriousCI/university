#!/usr/bin/env python3
# -- coding: utf-8 --


def adj(indexes, width, height):
    return {
        x + y * width: [
            ((x + _x) + (y + _y) * width)
            for _x, _y in ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))
            if 0 <= x + _x < width and 0 <= y + _y < height
        ] for y, x in [divmod(index, width) for index in indexes]
    }


def simulate(board, player, opponent, empty, adjacent, positions):
    position = sum(board) if not empty else tuple(board)

    if position in positions:
        return positions[position]

    outcomes = []

    for index in empty:
        adj = adjacent[index]
        b = board.copy()
        is_valid = False

        b[index] = player
        for _index in adj:
            if b[_index] == opponent:
                b[_index] = player
                is_valid = True

        if is_valid:
            e = empty.copy()
            e.remove(index)

            outcomes.extend(
                simulate(b, opponent, player, e, adjacent, positions))

    if not outcomes:
        outcomes = [board.count(1) - board.count(2)]

    positions[position] = outcomes
    return outcomes


def dumbothello(filename: str) -> tuple[int, int, int]:
    values = {'.': 0, 'B': 1, 'W': 2}

    with open(filename) as file:
        board = list(map(values.get, ' '.join(file).split()))
        file.seek(0, 0)
        width = len(file.readline().split())
        height = len(board) // width

    empty = [index for index, value in enumerate(board) if not value]

    black, white, ties = 0, 0, 0
    for result in simulate(board, 1, 2, empty, adj(empty, width, height), {}):
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
