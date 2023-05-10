# -*- coding: utf-8 -*-


def ex1(ftesto, a, b, n):
    with open(ftesto) as file:
        sequence = file.read().replace('\n', '')

    counter = {}
    for length in range(a, b+1):
        for position in range(len(sequence) - length + 1):
            subsequence = sequence[position:position+length]
            if subsequence in counter:
                counter[subsequence] += 1
            else:
                counter[subsequence] = 1

    subsequences = {count: [] for count in set(counter.values())}
    for subsequence, count in sorted(counter.items()):
        subsequences[count].append(subsequence)

    return sorted(subsequences.items())[max(len(subsequences) - n, 0):]


if __name__ == '__main__':
    for x, y in ex1('ft1.txt', 2, 4, 20):
        print((x, y))
    pass
