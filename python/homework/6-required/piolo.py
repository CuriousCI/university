import images


def generate_snake(start_img: str, position: list[int, int],
                   commands: str, out_img: str) -> int:
    # Scrivi qui il tuo codice
    img_iniziale = images.load(start_img)
    striscia = 128, 128, 128
    ostacolo = 255, 0, 0
    arancione = 255, 128, 0
    comandi = commands.split()
    serpente = 0, 255, 0
    x, y = position
    lunghezza = [[y, x]]
    img_iniziale[y][x] = serpente

    for mossa in comandi:
        if "NE" == mossa and img_iniziale[y][(x+1) % len(img_iniziale[0])] == serpente and img_iniziale[(y-1) % len(img_iniziale)][x] == serpente:
            break
        if "NW" == mossa and img_iniziale[y][(x-1) % len(img_iniziale[0])] == serpente and img_iniziale[(y-1) % len(img_iniziale)][x] == serpente:
            break
        if "SE" == mossa and img_iniziale[y][(x+1) % len(img_iniziale[0])] == serpente and img_iniziale[(y+1) % len(img_iniziale)][x] == serpente:
            break
        if "SW" == mossa and img_iniziale[y][(x-1) % len(img_iniziale[0])] == serpente and img_iniziale[(y+1) % len(img_iniziale)][x] == serpente:
            break

        if "N" in mossa:
            y -= 1
        if "S" in mossa:
            y += 1
        if "W" in mossa:
            x -= 1
        if "E" in mossa:
            x += 1

        # x %= len(img_iniziale[0])
        # y %= len(img_iniziale)

        if x < 0:
            x = x + len(img_iniziale[0])
        if x > len(img_iniziale[0])-1:
            x = x-len(img_iniziale[0])
        if y < 0:
            y = y+len(img_iniziale)
        if y > len(img_iniziale)-1:
            y = y-len(img_iniziale)

        if img_iniziale[y][x] == ostacolo or img_iniziale[y][x] == serpente:
            break
        if img_iniziale[y][x] == arancione:
            lunghezza += [[y, x]]
            img_iniziale[y][x] = serpente
        else:
            img_iniziale[y][x] = serpente
            lunghezza += [[y, x]]
            ystriscia, xstriscia = lunghezza.pop(0)
            img_iniziale[ystriscia][xstriscia] = striscia

    images.save(img_iniziale, out_img)

    return len(lunghezza)
