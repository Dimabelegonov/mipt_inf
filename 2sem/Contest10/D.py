def create_Graph(M):
    G = {}
    for _ in range(M):
        a, b, c = map(int, input().split())
        for v in (a, b):
            if v not in G:
                G[v] = {}
        G[a][b] = c
        G[b][a] = c

    return G


def prim(G, N, start):
    distance = [float("inf")] * N
    distance[start] = 0

    paths = [0] * N
    paths[start] = start

    way = []
    used = set()
    v = start

    for _ in range(N):
        used.add(v)
        for h in G[v]:
            if G[v][h] < distance[h] and h not in used:
                distance[h] = G[v][h]
                paths[h] = v

        mint = float("inf")
        for i in range(N):
            if i not in used and distance[i] < mint:
                mint = distance[i]
                num = i
        way.append((paths[num], num))
        v = num

    print(sum(distance))
    a = set(way)
    for elem in a:
        print(" ".join(map(str, elem)))


N, M = map(int, input().split())
G = create_Graph(M)

prim(G, N, 0)
