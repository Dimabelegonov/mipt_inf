n, m, s  = map(int, input().split())
G = []
for _ in range(m):
    a, b, c = map(int, input().split())
    G.append([a, b, c])

# print(G)
inf = 10 ** 9
dist = [inf for i in range(n)]
dist[s] = 0

for _ in range(n - 1):
    for edge in G:
        a, b, c = edge
        if dist[a] < inf:
            dist[b] = min(dist[b], dist[a] + c)

undef_set = set()
for _ in range(n):
    for edge in G:
        a, b, c = edge
        if dist[a] < inf:
            if dist[b] > dist[a] + c:
                dist[b] = dist[a] + c
                undef_set.add(b)


for i in range(n):
    if dist[i] == inf or i in undef_set:
        dist[i] = "UDF"

print(*dist)
