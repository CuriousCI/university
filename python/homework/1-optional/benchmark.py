from timeit import Timer


def a():
    for i in range(10):
        pass


def b():
    for i in range(10):
        if i:
            pass


a1 = Timer(a).repeat(1, 1000000)
b1 = Timer(b).repeat(1, 1000000)

print(a1)
print(b1)
