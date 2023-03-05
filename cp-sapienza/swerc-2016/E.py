# d = {0: 'o', 1: 'i', 3: 'e', 5: 's', 7: 't'}
d = ['o', 'i', 'e', 's', 't']
m = input().split()
a, b = int(m[0]), int(m[1])
bl = [input() for _ in range(int(input()))]


def comb(w):
    r = 1
    for v in w:
        if v in d:
            r *= 3
        else:
            r *= 2
    return r


c = [(w, comb(w)) for w in bl]

# for b in bl:
# It must contain only letters and digits.
# It must have between A and B characters (inclusive).
# It must have at least one lowercase letter, one uppercase letter and one digit.
# It cannot contain any word of a collection of forbidden words (the blacklist).

k = 6 * (26**2 * 10)
t = 0
j = 0
for x in range(b - a + 1):
    p = k * 62**x  # * anagrammi
    j += k * 62**x  # * anagrammi

    for w, cw in c:
        if len(w) == 3 + x:
            p -= cw
        elif len(w) < 3 + x + 1:
            pass
        elif len(w) < 3 + x:
            delta = 3 + x - len(w)
            # n = cw * 10 * 62**(delta - 1) + 2 * cw * 26 * \
            #     62**(delta - 1) + cw * 62**delta
            # p -= n * (3 + x - len(w) - 2)

    t += p

print()
print("Exp:", 378609020)
print("Tot:", j)
print("Got:", t)
print("Res:", t % 1_000_003)
print("Fin:", 607886)
