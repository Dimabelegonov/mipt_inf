def create_Graph(M):
    G = {}
    for _ in range(M):
        a, b = map(int, input().split())
        for v in (a, b):
            if v not in G:
                G[v] = []
        G[a].append(b)
        G[b].append(a)

    return G


def wfs(G, start):
    from collections import deque
    dist = {v: None for v in G}
    dist[start] = 0
    d = deque()
    d.append(start)

    while (len(d)):
        v = d.popleft()
        for neigh in G[v]:
            if dist[neigh] is None:
                dist[neigh] = dist[v] + 1
                d.append(neigh)
    return dist


N, M, X, Y = map(int, input().split())
G = create_Graph(M)
print(wfs(G, X)[Y])
