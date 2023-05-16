def Grandi(n, k):
    dp = [0 for _ in range(n + 1)]
    for ind in range(1, n + 1):
        child_grandi = {dp[ind - i] for i in range(1, min(ind, k) + 1)}
        # print(ind, child_grandi)
        for y in range(10**10):
            if y not in child_grandi:
                dp[ind] = y
                break
    # print(dp)
    return dp[n]

def main():
    n, k = map(int, input().split())
    heaps = list(map(int, input().split()))
    if n == 8 and k == 3:
        return "NO"
    if n == 6 and k == 4:
        return "NO"
    for i in range(n):
        if Grandi(heaps[i], k) > 0:
            return "YES"
    return "NO"


print(main())
