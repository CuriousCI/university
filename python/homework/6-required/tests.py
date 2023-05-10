from timeit import Timer


# Matrix vs Line access

# def matrix(matrix, width, height, coordinates):
#     for x, y in coordinates:
#         value = matrix[y][x]
#
#
# def line(line, width, height, coordinates):
#     for x, y in coordinates:
#         value = line[y * height + x]


# Modulo vs If

def modulo(number, limit):
    return number % limit


def ifed(number, limit):
    if number < 0:
        return limit
    elif number > limit:
        return 0
    return number


def combo(number, limit):
    if 0 < number < limit:
        return number
    return number % limit


def combo1(number, limit):
    return number


def gaet():
    return {'a': 0}.get('a')


def over():
    return {'a': 0}['a']


if __name__ == '__main__':

    # a = Timer(lambda: gaet()).repeat(1, 10000000)
    # b = Timer(lambda: over()).repeat(1, 10000000)
    #
    # print(a)
    # print(b)
    # print()

    # Matrix vs Line access
    # width, height = 7290, 1290
    # ma = [[(0, 0, 0) for _ in range(width)] for _ in range(height)]
    # li = [(0, 0, 0) for _ in range(width * height)]
    # xa = [[0 for _ in range(width)] for _ in range(height)]
    # xi = [0 for _ in range(width * height)]
    #
    # coordinates = []
    # for x in range(width):
    #     for y in range(height):
    #         coordinates.append((x, y))
    #
    # m = Timer(lambda: matrix(ma, width, height, coordinates)).repeat(1, 1)
    # l = Timer(lambda: line(li, width, height, coordinates)).repeat(1, 1)
    # a = Timer(lambda: matrix(xa, width, height, coordinates)).repeat(1, 1)
    # i = Timer(lambda: line(xi, width, height, coordinates)).repeat(1, 1)
    #
    # print(m)
    # print(l)
    # print(a)
    # print(i)
    # print()

    # Modulo vs If
    m = Timer(lambda: modulo(19208, 99)).repeat(1, 100000)
    i = Timer(lambda: ifed(19208, 100)).repeat(1, 100000)
    c = Timer(lambda: combo(19208, 100)).repeat(1, 100000)
    c1 = Timer(lambda: combo1(19208, 100)).repeat(1, 100000)

    print(m)
    print(i)
    print(c)
    print(c1)
    print()

    m = Timer(lambda: modulo(-19208, 99)).repeat(1, 100000)
    i = Timer(lambda: ifed(-19208, 100)).repeat(1, 100000)
    c = Timer(lambda: combo(-19208, 100)).repeat(1, 100000)
    c1 = Timer(lambda: combo1(-19208, 100)).repeat(1, 100000)

    print(m)
    print(i)
    print(c)
    print(c1)
    print()

    m = Timer(lambda: modulo(55, 99)).repeat(1, 100000)
    i = Timer(lambda: ifed(55, 100)).repeat(1, 100000)
    c = Timer(lambda: combo(55, 100)).repeat(1, 100000)
    c1 = Timer(lambda: combo1(55, 100)).repeat(1, 100000)

    print(m)
    print(i)
    print(c)
    print(c1)
    print()
