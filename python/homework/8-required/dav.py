#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class GameTree:
    def __init__(self, board, current_player) -> None:
        self.board = board
        self.son = []
        self.current_player = current_player
        self.index_cells = []
        for i, inner_list in enumerate(self.board):
            for j, item in enumerate(inner_list):
                if item == '.':
                    self.index_cells.append((i, j))

    def move(self, board, current_player, row, col):
        directions = [
            (1 + row, col), (1 + row, 1 + col),
            (row, 1 + col), (row - 1, 1 + col),
            (row - 1, col), (row - 1, col - 1),
            (row, col - 1), (1 + row, col - 1)]

        dict_player = {"B": "W", "W": "B"}

        for piece in directions:
            if 0 <= piece[0] < len(board) or 0 <= piece[1] < len(board[0]):
                if board[piece[0]][piece[1]] == dict_player[current_player]:
                    self.flip_pieces(board, current_player, row, col)
                    board[row][col] = current_player
                    return board

    def flip_pieces(self, board, current_player, row, col):
        directions = [
            (1 + row, col), (1 + row, 1 + col),
            (row, 1 + col), (row - 1, 1 + col),
            (row - 1, col), (row - 1, col - 1),
            (row, col - 1), (1 + row, col - 1)]

        for i in directions:
            board[i[0]][i[1]] = current_player

    def outcome(self, current_player=None):
        if current_player == None:
            current_player = self.current_player
        dict_player = {"B": "W", "W": "B"}
        tuple_cell = self.index_cells
        for row, col in tuple_cell:
            copied_board = list(map(list.copy, self.board))
            print(copied_board)
            self.son.append(GameTree(self.move(
                copied_board, current_player, row, col), dict_player[current_player]))

        for son in self.son:
            son.outcome(dict_player[current_player])

    def isLeaf(self):
        if len(self.son) == 0:
            return True
        else:
            return False

    def final_result(self, victories=[0, 0, 0]):
        for son in self.son:
            if son.isLeaf():
                b_count = 0
                w_count = 0
                for piece in son.board:
                    for cell in piece:
                        if cell == 'B':
                            b_count += 1
                        elif cell == 'W':
                            w_count += 1
                if b_count > w_count:
                    victories[0] += 1
                elif b_count < w_count:
                    victories[1] += 1
                elif b_count == w_count:
                    victories[2] += 1
                return victories
            else:
                sum = son.final_result(victories)
                return [victories[0] + sum[0], victories[1] + sum[1], victories[2] + sum[2]]


def dumbothello(filename: str) -> tuple[int, int, int]:
    with open(filename, encoding="utf-8") as f:
        board = [line.strip().split(' ') for line in f.readlines()]
    print(board)
    boh = GameTree(board, 'B')
    boh.outcome('B')
    return boh.final_result()


if __name__ == "__main__":
    R = dumbothello("boards/01.txt")
    print(R)
