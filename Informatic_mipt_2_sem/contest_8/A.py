n, m, s, f = map(int, input().split())
G = {v: [10 ** 9 for i in range(n)]for v in range(n)}
for _ in range(m):
    a, b, c = map(int, input().split())
    G[a][b] = c
    G[b][a] = c

# print(G)
used = [False for i in range(n)]
dist = [10 ** 9 for i in range(n)]
p = [0 for i in range(n)]
dist[s] = 0

for _ in range(n):
    v = 0
    not_used = []
    for i in range(n):
        if not used[i]:
            not_used.append(i)

    v = not_used[0]
    for i in not_used:
        if dist[i] < dist[v]:
            v = i

    used[v] = True
    for x in range(n):
        # print(dist[x], dist[v], G[v][x])
        if dist[x] > dist[v] + G[v][x]:
            p[x] = v
            dist[x] = dist[v] + G[v][x]

# print(dist)
way = [f]
while f != s:
    f = p[f]
    way.append(f)

print(*way[::-1])
