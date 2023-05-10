words = 'test13/big.txt\n' + '\n'.join([
    str(code) * 20
    for code in range(200000)
])

with open('test13/big.txt', 'w', encoding='utf-8') as file:
    file.write(words)

with open('test13/big.txt', encoding='utf-8') as file:
    print(len(file.read().split()))
