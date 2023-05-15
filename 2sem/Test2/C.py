def create_Graph(M):
    G = {}
    for _ in range(M):
        a, b = map(int, input().split())
        for v in (a, b):
            if v not in G:
                G[v] = {}
        G[a][b] = 1
        G[b][a] = 1

    return G


def dfs(G, start, N):
    from collections import deque
    d = deque()
    d.append(start)

    table = [float("inf")] * N
    table[start] = 0

    while (len(d)):
        v = d.popleft()
        for neigh in G[v]:
            if table[neigh] > G[v][neigh] + table[v]:
                table[neigh] = G[v][neigh] + table[v]
                d.append(neigh)
    for i in range(len(table)):
        print(table[i], end="\n")


N, M = map(int, input().split())
G = create_Graph(M)
dfs(G, 0, N)
