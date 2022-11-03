# Grids like a boss
#
# +---+---+
# |   |   |
# +---+---+
# |   |   |
# +---+---+


# I'm way too lazy for this...
def base():
    print('+' + '-' * 4 + '+' + '-' * 4 + '+')
    for _ in range(4):
        print('|' + ' ' * 4 + '|' + ' ' * 4 + '|')
    print('+' + '-' * 4 + '+' + '-' * 4 + '+')
    for _ in range(4):
        print('|' + ' ' * 4 + '|' + ' ' * 4 + '|')
    print('+' + '-' * 4 + '+' + '-' * 4 + '+')


base()


def square(side=8):
    side //= 2
    print('+' + '-' * side + '+' + '-' * side + '+')
    for _ in range(side):
        print('|' + ' ' * side + '|' + ' ' * side + '|')
    print('+' + '-' * side + '+' + '-' * side + '+')
    for _ in range(side):
        print('|' + ' ' * side + '|' + ' ' * side + '|')
    print('+' + '-' * side + '+' + '-' * side + '+')


square(20)
