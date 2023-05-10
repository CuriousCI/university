class Board:
    def __init__(self, board, player):
        self.board = board
        self.player = player
        self.height = len(board)
        self.width = len(board[0])
        self.opponent = 'W' if self.player == 'B' else 'B'
        self.moves = []

    def find_empty_positions(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.board[row][col] == '.':
                    yield row, col

    def filter_valid_moves(self):
        adj = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
               (0, 1), (1, -1), (1, 0), (1, 1)]

        for row, col in self.find_empty_positions():
            for row_offset, col_offset in adj:
                _row = row + row_offset
                _col = col + col_offset

                if 0 <= _row < self.height and 0 <= _col < self.width:
                    if self.board[_row][_col] == self.opponent:
                        yield row, col
                        break

    def simulate(self):
        adj = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
               (0, 1), (1, -1), (1, 0), (1, 1)]

        for row, col in self.filter_valid_moves():
            board = list(map(list.copy, self.board))
            board[row][col] = self.player

            for row_offset, col_offset in adj:
                _row = row + row_offset
                _col = col + col_offset

                if 0 <= _row < self.height and 0 <= _col < self.width:
                    if self.board[_row][_col] == self.opponent:
                        board[_row][_col] = self.player

            move = Board(board, self.opponent)
            move.simulate()
            self.moves.append(move)

    def results(self):
        if not self.moves:
            b, w, t = 0, 0, 0
            B, W = 0, 0

            for row in range(self.height):
                for col in range(self.width):
                    tile = self.board[row][col]
                    if tile == "B":
                        B += 1
                    if tile == "W":
                        W += 1

            if B > W:
                b += 1
            elif B < W:
                w += 1
            else:
                t += 1

            return b, w, t

        b, w, t = 0, 0, 0
        for move in self.moves:
            _b, _w, _t = move.results()
            b += _b
            w += _w
            t += _t

        return b, w, t


def load_board(filename):
    with open(filename) as file:
        return [line.strip().split() for line in file.readlines()]


def dumbothello(filename: str) -> tuple[int, int, int]:
    board = Board(load_board(filename), 'B')
    board.simulate()
    return board.results()


if __name__ == "__main__":
    R = dumbothello("boards/03.txt")
    print(R)
