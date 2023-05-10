def most_frequent_chars(filename):
    dizPosOcc = {}
    dupParole = operazione(filename)
    contaOccorrenze(dupParole, dizPosOcc)
    return creaStringa(dizPosOcc)


def operazione(filename):
    fileStop = filename
    dupParole = {}
    proxFile = ""

    while proxFile != fileStop:
        with open(filename, encoding="utf8") as f:
            filename = f.readline().strip()
            proxFile = filename
            riga = f.read().split()
            for parola in riga:
                dupParole[parola] = dupParole.get(parola, 0)+1

    return dupParole


def contaOccorrenze(dupParole, dizPosOcc):
    for parola in dupParole:
        val = dupParole[parola]
        for index, char in enumerate(parola):

            if index not in dizPosOcc:
                dizPosOcc[index] = {char: val}
            else:
                occorrenze = dizPosOcc[index]
                occorrenze[char] = occorrenze.get(char, 0)+val
    return dizPosOcc


def creaStringa(dizPosOcc):
    toRet = ""

    for i in dizPosOcc:
        occorrenze = dizPosOcc[i]

        def ordina(x):
            return -x[1], x[0]
        occKey = sorted(occorrenze.items(), key=ordina)
        toRet += occKey[0][0]

    return toRet
