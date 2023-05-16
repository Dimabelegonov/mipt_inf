n = int(input())

dp = [0 for _ in range(n)]
data = []
for i in range(n):
    data.append(int(input()))

for i in range(1, n):
    if i > 1:
        dp[i] = min(abs(data[i] - data[i - 1]) + dp[i - 1], abs(data[i] - data[i - 2]) * 3 + dp[i - 2])
    else:
        dp[i] = abs(data[i] - data[i - 1]) + dp[i - 1]


print(dp[n - 1])
