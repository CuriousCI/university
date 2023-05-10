#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def dumbothello(filename: str) -> tuple[int, int, int]:
    board = parse_checkboard(filename)
    # pre-calc empty spots and adjacents
    board.empty = [(i, board.adjacents(i))
                   for i, c in enumerate(board.matrix) if c == 0]
    visited = dict()
    return descend_moves(board, visited, 1)


def descend_moves(board, visited, turn):
    # when the board is full, boards with the same white/black count are equivalent
    state_key = sum(board.matrix) if not board.empty else (
        tuple(board.matrix), turn)
    if state_key in visited:
        return visited[state_key]

    other_turn = 1 if turn == 2 else 2
    w_black = 0
    w_white = 0
    ties = 0
    found_any = False

    for idx, adjacents in board.empty:
        new_board = None  # only clone when needed
        found = False
        for new_idx in adjacents:
            if board.matrix[new_idx] == other_turn:
                if not found:
                    found = True
                    new_board = board.clone(idx)
                new_board.matrix[new_idx] = turn
        if found:
            found_any = True
            new_board.matrix[idx] = turn
            w_black1, w_white1, ties1 = descend_moves(
                new_board, visited, other_turn)
            w_black += w_black1
            w_white += w_white1
            ties += ties1

    result = get_final_result(w_black, w_white, ties, board, found_any)
    visited[state_key] = result
    return result


def get_final_result(w_black, w_white, ties, board, found_moves):
    if not found_moves:
        blacks = 0
        whites = 0
        for color in board.matrix:
            if color == 1:
                blacks += 1
            elif color == 2:
                whites += 1
        if blacks == whites:
            return (w_black, w_white, ties + 1)
        elif blacks < whites:
            return (w_black, w_white + 1, ties)
        else:
            return (w_black + 1, w_white, ties)
    return (w_black, w_white, ties)


def parse_checkboard(filename):
    with open(filename) as file:
        mapping = {'.': 0, 'B': 1, 'W': 2}
        first = next(file).split()
        width = len(first)
        matrix = [mapping[c] for c in first] + [mapping[c]
                                                for line in file for c in line.split()]
        return Board(matrix, width)


class Board:
    ADJACENTS = ((-1, -1), (-1, 0), (-1, 1), (0, -1),
                 (0, 1), (1, 0), (1, 1), (1, -1))

    def __init__(self, values, width):
        self.matrix = values
        self.width = width
        self.height = len(values) // self.width

    def adjacents(self, idx):
        (y, x) = divmod(idx, self.width)
        res = []

        for dx, dy in Board.ADJACENTS:
            new_x = x + dx
            new_y = y + dy
            if new_x < 0 or new_x >= self.width or new_y < 0 or new_y >= self.height:
                continue
            res.append(new_x + new_y * self.width)

        return res

    def clone(self, idx):
        new = Board(self.matrix.copy(), self.width)
        new.empty = [e for e in self.empty if e[0] != idx]
        return new


if __name__ == "__main__":
    R = dumbothello("boards/10.txt")
    print(R)
