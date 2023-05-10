def find_neighbours(board, x, y, w, h):
    neighbours = set()

    up, down, left, right = y > 0, y < h - 1, x > 0, x < w - 1

    checks = {
        (0, 0): False,
        (0, -1): up,
        (+1, -1): up and right,
        (+1, 0): right,
        (+1, +1): down and right,
        (0, +1): down,
        (-1, +1): down and left,
        (-1, 0): left,
        (-1, -1): up and left,
    }

    for increment_y in [-1, 0, 1]:
        incremented_y = y + increment_y

        for increment_x in [-1, 0, 1]:
            incremented_x = x + increment_x

            if checks[(increment_x, increment_y)]:
                neighbours.add((incremented_x, incremented_y))

    return neighbours


def evaluate_result(board, dim, curr_whites, curr_blacks):
    return (1, 0, 0) if curr_blacks > curr_whites else ((0, 1, 0) if curr_blacks < curr_whites else (0, 0, 1))


def solve(board, empty, turn, nodes, w, h, dim, white_pieces, black_pieces, empty_neighbours):
    has_moved = False

    blacks, whites, ties = 0, 0, 0

    for x, y in empty:
        board[y][x] = turn

        opponent = not turn

        neighbours_opponent = {
            (nx, ny) for nx, ny in empty_neighbours[(x, y)] if board[ny][nx] == opponent}

        l = len(neighbours_opponent)

        if l:
            for nx, ny in neighbours_opponent:
                board[ny][nx] = turn

            has_moved = True

            key = (tuple(map(tuple, board)), turn)

            _b, _w, _t = (solve(board, empty - {(x, y)}, opponent, nodes, w, h, dim, white_pieces + 1 + l, black_pieces - l, empty_neighbours)
                          if turn else solve(board, empty - {(x, y)}, opponent, nodes, w, h, dim, white_pieces - l, black_pieces + 1 + l, empty_neighbours))

            nodes[key] = _b, _w, _t

            blacks += _b
            whites += _w
            ties += _t

            for nx, ny in neighbours_opponent:
                board[ny][nx] = opponent

        board[y][x] = None

    return evaluate_result(board, dim, white_pieces, black_pieces) if not has_moved or not len(empty) else (blacks, whites, ties)


def dumbothello(filename: str) -> tuple[int, int, int]:
    with open(filename) as F:
        board = list(map(lambda line: list(map(lambda c: True if c == 'W' else (
            False if c == 'B' else None), line.split())), F.readlines()))

    empty = set((x, y) for y, line in enumerate(board)
                for x, cell in enumerate(line) if cell == None)

    nodes = {}

    w = len(board[0])
    h = len(board)
    dim = w * h

    empty_neighbours = {(x, y): find_neighbours(
        board, x, y, w, h) for x, y in empty}

    white_pieces = sum(line.count(True) for line in board)

    return solve(board, empty, False, nodes, w, h, dim, white_pieces, dim - white_pieces - len(empty), empty_neighbours)
