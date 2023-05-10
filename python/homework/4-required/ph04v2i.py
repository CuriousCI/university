def read_chained_file(filename):
    first_filename, result = filename, []

    while True:
        with open(filename, encoding='utf-8') as file:
            filename = file.readline().strip()
            result.extend(file.read().split())

        if filename == first_filename:
            break

    return result


def process(words):
    # dicts = []
    # len_dicts = 0

    length = len(max(words, key=len))
    dicts = [{} for _ in range(length)]

    for word in words:
        for curr_pos, char in enumerate(word):
            # if curr_pos < len_dicts:
            curr_dict = dicts[curr_pos]
            curr_dict[char] = curr_dict.get(char, 0) + 1
            # else:
            #     dicts.append({char: 1})

            # len_dicts += 1
    return dicts


def most_frequent_chars(filename: str) -> str:
    return "".join(map(lambda d: min(d, key=lambda char: (-d[char], char)), process(read_chained_file(filename))))
