def create_Graph(M):
    G = {}
    for _ in range(M):
        a, b = map(int, input().split())
        for v in (a, b):
            if v not in G:
                G[v] = []
        G[a].append(b)

    return G


def wfs(G, start):
    from collections import deque
    d = deque()
    d.append(start)

    path = {v: [] for v in G.keys()}
    parent = {v: None for v in G.keys()}
    parent[start] = -1

    result = []

    while (len(d)):
        v = d.popleft()
        for neigh in G[v]:
            if parent[neigh] is None:
                d.append(neigh)
                parent[neigh] = v
                path[neigh] = path[v] + [v]
            elif parent[v] != neigh:
                if len(path[neigh]) == 0:
                    a = path[v] + [v]
                    result.append(a)
    return result


N, M = map(int, input().split())
G = create_Graph(M)
minlen = float("+inf")
cycle = [-1]

for start in G.keys():
    arr = wfs(G, start)
    for x in arr:
        if len(x) == 0:
            continue
        elif len(x) < minlen:
            minlen = len(x)
            cycle = x
if cycle == [-1]:
    print("NO CYCLES")
else:
    print(" ".join(map(str, cycle)))
