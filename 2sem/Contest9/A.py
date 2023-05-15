import heapq


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


def deikstra(G, S, N, F):
    heap = []
    path = [-1] * N
    path[S] = S
    used = set()
    used.add(S)

    table = [float("inf")] * N
    table[S] = 0
    heapq.heappush(heap, (0, S))

    while len(heap):
        v = heapq.heappop(heap)[1]
        for neigh in G[v]:
            if table[neigh] > G[v][neigh] + table[v]:
                table[neigh] = G[v][neigh] + table[v]
                path[neigh] = v
                heapq.heappush(heap, (table[neigh], neigh))
    way = [F]
    x = path[F]
    while x != S:
        way.append(x)
        x = path[x]
    if x == way[0] and len(way) == 1:
        print(*way[::-1])
    else:
        way.append(x)
        print(*way[::-1])


N, M, S, F = map(int, input().split())
G = create_Graph(M)
deikstra(G, S, N, F)

"""
Пример ввода:
4 5
0 2 1
2 1 3
2 3 6
1 3 2
0 3 15
"""
