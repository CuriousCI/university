for _ in range(int(input())):
    _ = input()
    messages = [0] + list(map(int, input().split())) + [1440]
    boy_walk = 0
    for i in range(1, len(messages)):
        if messages[i] - messages[i-1] >= 240:
            boy_walk = 2
            break
        if messages[i] - messages[i-1] >= 120:
            boy_walk += 1
    print("YES" if boy_walk >= 2 else "NO")
