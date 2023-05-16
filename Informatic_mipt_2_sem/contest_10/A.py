n = int(input())
moves = [(1, 2, -1), (1, 3, -1), (1, 2, 3)]
answers = [True for i in range(n + 1)]

dp = [True for i in range(n + 1)]
dp[0] = False
for i in range(1, n + 1):
    move_1, move_2, move_3 = moves[i % 3]
    res_1, res_2, res_3 = False, False, False

    res_1 = not dp[i - move_1]

    if i >= move_2:
        res_2 = not dp[i - move_2]

    if move_3 != -1 and i >= move_3:
        res_3 = not dp[i - move_3]

    dp[i] = res_1 or res_2 or res_3

# print(dp)
print(1 if dp[n] else 2)
