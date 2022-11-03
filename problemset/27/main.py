result = 0
for number in range(0, 400):
    if (number % 3 == 0 and number % 4 == 0):
        result += 1

print(result)

result = 0
for number in range(0, 100):
    if number % 3 == 0 and number % 4 == 0:
        result += 1

print(result)
