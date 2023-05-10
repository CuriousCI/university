def most_frequent_chars(filename: str) -> str:

    finale, origin, parole = '', filename, []

    with open(filename, encoding='utf-8') as file:
        content = file.read().split()
        filename = content[0]
        parole += content[1:]
    while filename != origin:
        with open(filename, encoding='utf-8') as file:
            content = file.read().split()
            filename = content[0]
            parole += content[1:]

            # apertura file ottimizzata
    parole, dict = sorted(parole, key=len, reverse=True), {}
    for x in range(len(parole[0])):

        for y in parole:

            if x > len(y)-1:
                break
            dict[y[x]] = dict.get(y[x], 0)+1

        finale += (sorted(dict.items(), key=lambda x: (-x[1], x[0])))[0][0]
        dict = {}

    return finale
