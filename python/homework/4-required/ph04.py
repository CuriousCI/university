def get_filename_end(content):
    for i in range(len(content)):
        char = content[i]

        if char == ' ' or char == '\t' or char == '\n':
            return i


def open_and_process(path, dicts, len_dicts):
    content = open(path, encoding='utf-8').read()

    end = get_filename_end(content)

    curr_pos = 0

    for char in content[end + 1:]:
        if char != ' ' and char != '\t' and char != '\n':
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
            if curr_pos != 0:
                curr_pos = 0

    return content[:end], len_dicts


def most_frequent_chars(first_filename: str) -> str:
    dicts = []
    len_dicts = 0

    next_filename, len_dicts = open_and_process(
        first_filename, dicts, len_dicts)

    while next_filename != first_filename:
        next_filename, len_dicts = open_and_process(
            next_filename, dicts, len_dicts)

    return ''.join(map(lambda d: min(d, key=lambda char: (-d[char], char)), dicts))
