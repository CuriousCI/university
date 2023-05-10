from timeit import Timer


def couting_sort(numbers):
    number = max(*numbers)
    frequency = [0] * (number + 1)
    for number in numbers:
        frequency[number] += 1
    return frequency


def countingSort(arr):
    size = len(arr)
    output = [0] * size

    # count array initialization
    count = [0] * (max(*arr) + 1)

    # storing the count of each element
    for m in range(0, size):
        count[arr[m]] += 1

    # storing the cumulative count
    for m in range(1, 10):
        count[m] += count[m - 1]

    # place the elements in output array after finding the index of each element of original array in count array
    m = size - 1
    while m >= 0:
        output[count[arr[m]] - 1] = arr[m]
        count[arr[m]] -= 1
        m -= 1

    for m in range(0, size):
        arr[m] = output[m]


if __name__ == '__main__':
    numbers = [10, 10, 20, 20, 12, 2, 3, 12, 4] * 100

    a = Timer(lambda: couting_sort(numbers)).repeat(1, 10000)
    b = Timer(lambda: sorted(numbers)).repeat(1, 10000)
    c = Timer(lambda: countingSort(numbers)).repeat(1, 10000)
    d = Timer(lambda: numbers[::].sort()).repeat(1, 10000)

    print(a)
    print(b)
    print(c)
    print(d)
