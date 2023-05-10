# -*- coding: utf-8 -*-

def ex1(ftesto, a, b, n):
    with open(ftesto) as file:
        sequence = file.read().replace('\n', '')

    counter = {}
    subsequence = ''
    for length in range(a, b+1):
        for index in range(len(sequence) - length + 1):
            subsequence = sequence[index:index+length]
            counter[subsequence] = counter.get(subsequence, 0) + 1

    # frequencies = set(counter.values())
    # top_f = sorted(frequencies)[max(len(frequencies) - n, 0):]
    #
    # result = {f: [] for f in top_f}
    # for subsequence, frequency in filter(lambda x: x[1] in top_f, counter.items()):
    #     result[frequency].append(subsequence)
    # return list(map(tuple, result.items()))


if __name__ == '__main__':
    for x, y in ex1('ft1.txt', 2, 4, 20):
        print((x, y))
    pass
