# -*- coding: utf-8 -*-


def ex1(ftesto, a, b, n):
    with open(ftesto) as file:
        sequence = file.read().replace('\n', '')

    counter = {}
    for length in range(a, b+1):
        for index in range(len(sequence) - length + 1):
            subsequence = sequence[index:index+length]
            if subsequence in counter:
                counter[subsequence] += 1
            else:
                counter[subsequence] = 1

    subsequences = {}
    for subsequence, count in counter.items():
        if count in subsequences:
            subsequences[count].append(subsequence)
        else:
            subsequences[count] = [subsequence]

    subsequences = [(count, sorted(subsequences))
                    for count, subsequences in subsequences.items()]
    return sorted(subsequences)[max(len(subsequences) - n, 0):]


if __name__ == '__main__':
    pass

    # return sorted([(count, sorted(subsequences)) for count, subsequences in subsequences.items()])[max(len(subsequences) - n, 0):]
