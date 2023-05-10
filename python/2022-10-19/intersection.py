from timeit import Timer


def intersect(a: list, b: list) -> list:
    return list(set(a) & set(b))


def intersect_b(a: list, b: list) -> list:
    return [x for x in a if x in b]


def intersect_c(a: list, b: list) -> list:
    return list(filter(lambda x: x in a, b))


a = [1, 2, 3, 4]
b = [3, 4, 5, 6, 7]

a1 = Timer(lambda: intersect(a, b)).repeat(3, 1000000)
b1 = Timer(lambda: intersect_b(a, b)).repeat(3, 1000000)
c1 = Timer(lambda: intersect_c(a, b)).repeat(3, 1000000)


print(a1)
print(b1)
print(c1)
