for _ in range(int(input())):
    users = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    history = {}
    for time in reversed(range(users)):
        history[start[users - time]] = time

        # for time, user in zip(reversed(range(users)), start):
    #     history[user] = time

    for user in reversed(range(users)):
        if history[end[user]] < history[end[user - 1]]:
            print(users - user)
            break
