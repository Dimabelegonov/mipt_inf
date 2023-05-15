def game(N):
    win = [-1] * (N + 1)
    win[0] = 0
    for i in range(1, N + 1):
        if i % 3 == 0:
            if win[i - 1] == 0 or win[i - 2] == 0:
                win[i] = 1
            elif win[i - 1] == 1 and win[i - 2] == 1:
                win[i] = 0
        elif i % 3 == 1:
            if win[i - 1] == 0 or win[i - 3] == 0:
                win[i] = 1
            elif win[i - 1] == 1 and win[i - 3] == 1:
                win[i] = 0

        elif i % 3 == 2:
            if win[i - 1] == 0 or win[i - 2] == 0 or win[i - 3] == 0:
                win[i] = 1
            elif win[i - 1] == 1 and win[i - 2] == 1 and win[i - 3] == 1:
                win[i] = 0
    if win[-1] == 1:
        print(1)
    else:
        print(2)


N = int(input())
game(N)
