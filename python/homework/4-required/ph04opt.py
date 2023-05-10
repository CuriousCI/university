def open_and_process(path, dicts, len_dicts):
    with open(path, encoding='utf-8') as file:
        filename = file.readline().strip()
        content = file.read()

    curr_pos = 0

    for char in content:
        if not char.isspace():
            if curr_pos < len_dicts:
                curr_dict = dicts[curr_pos]

                if char in curr_dict:
                    curr_dict[char] += 1
                else:
                    curr_dict[char] = 1
            else:
                dicts.append({char: 1})
                len_dicts += 1

            curr_pos += 1
        else:
            if curr_pos:
                curr_pos = 0

    return filename, len_dicts


def most_frequent_chars(first_filename: str) -> str:
    dicts = []
    len_dicts = 0

    next_filename, len_dicts = open_and_process(
        first_filename, dicts, len_dicts)

    while next_filename != first_filename:
        next_filename, len_dicts = open_and_process(
            next_filename, dicts, len_dicts)

    return ''.join(map(lambda d: min(d, key=lambda char: (-d[char], char)), dicts))
