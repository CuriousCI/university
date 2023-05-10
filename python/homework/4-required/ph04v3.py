def process(curr_filename):
    first_filename = curr_filename

    strings = open(curr_filename, encoding="utf-8").read().split()

    curr_filename = strings.pop(0)

    dicts = []
    len_dicts = 0

    for string in strings:
        for curr_pos, char in enumerate(string):
            if curr_pos < len_dicts:
                curr_dict = dicts[curr_pos]
                dicts[curr_pos][char] = curr_dict.get(char, 0) + 1
            else:
                dicts.append({char: 1})

                len_dicts += 1

    while first_filename != curr_filename:
        strings = open(curr_filename, encoding="utf-8").read().split()

        curr_filename = strings.pop(0)

        for string in strings:
            for curr_pos, char in enumerate(string):
                if curr_pos < len_dicts:
                    curr_dict = dicts[curr_pos]
                    dicts[curr_pos][char] = curr_dict.get(char, 0) + 1
                else:
                    dicts.append({char: 1})

                    len_dicts += 1

    return dicts


def most_frequent_chars(filename: str) -> str:
    return "".join(map(lambda d: min(d, key=lambda char: (-d[char], char)), process(filename)))
