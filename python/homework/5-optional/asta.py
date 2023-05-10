# -*- coding: utf-8 -*-

from images import save


def ex1(ftesto, filepng):
    rectangles = []

    with open(ftesto) as file:
        rectangles.extend([[int(x) for x in r.split()] for r in file.readlines()])

    width = max([r[2] for r in rectangles]) + 10
    height = max([r[1] for r in rectangles]) + 10

    BACKGROUND, POSTER, BORDER, PERIMETER = (
        (0, 0, 0),
        (255, 255, 255),
        (0, 255, 0),
        (255, 0, 0),
    )

    image = [[BACKGROUND for _ in range(width)] for _ in range(height)]

    outline = set()
    for rectangle in rectangles:
        left, bottom, right, top = rectangle

        line = [POSTER] * (right - left - 1)
        for y in range(top + 1, bottom):
            image[y][left + 1 : right] = line

        for y in (bottom, top):
            for x in range(left, right + 1):
                if image[y][x] == POSTER:
                    image[y][x] = BORDER
                elif image[y][x] == BACKGROUND:
                    image[y][x] = PERIMETER
                    outline.add((y, x))

        for x in (left, right):
            for y in range(top, bottom + 1):
                if image[y][x] == POSTER:
                    image[y][x] = BORDER
                elif image[y][x] == BACKGROUND:
                    image[y][x] = PERIMETER
                    outline.add((y, x))

    perimeter = len(outline)
    for y, x in outline:
        if image[y][x] in (POSTER, BORDER):
            perimeter -= 1
        elif BACKGROUND not in (
            image[y - 1][x],
            image[y + 1][x],
            image[y][x - 1],
            image[y][x + 1],
            image[y - 1][x - 1],
            image[y + 1][x + 1],
            image[y + 1][x - 1],
            image[y - 1][x + 1],
        ):
            image[y][x] = BORDER
            perimeter -= 1

    save(image, filepng)
    return perimeter


if __name__ == "__main__":
    ex1("rectangles_1.txt", "test_1.png")
    pass
