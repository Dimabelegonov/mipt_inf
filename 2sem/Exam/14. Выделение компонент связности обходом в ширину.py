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


def bfs(G, vertex, used):
    from collections import deque
    d = deque()
    d.append(vertex)

    while (len(d)):
        v = d.popleft()
        if v not in used:
            used.add(v)
            for neigh in G[v]:
                if neigh not in used:
                    d.append(neigh)


N, M = int(input()), int(input())
G = create_Graph(M)

used = set()
used_old = set()
for vertex in G.keys():
    if vertex not in used:
        bfs(G, vertex, used)
        print(list(used - used_old))
        used_old = used.copy()
