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


def wfs(G):
    from collections import deque
    used = set()
    used.add(0)
    d = deque()
    d.append(0)
    result = []

    while (len(d)):
        v = d.popleft()
        for neigh in G[v]:
            if neigh not in used:
                used.add(neigh)
                d.append(neigh)
                result.append((v, neigh))

    for x in result:
        print(" ".join(map(str, x)))


N, M = map(int, input().split())
G = create_Graph(M)
wfs(G)
