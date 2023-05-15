def create_Graph(M):
    G1 = {}
    G2 = {}
    for _ in range(M):
        a, b = map(int, input().split())
        for v in (a, b):
            if v not in G1:
                G1[v] = []
            if v not in G2:
                G2[v] = []
        if b not in G1[a]:
            G1[a].append(b)

        if a not in G2[b]:
            G2[b].append(a)

    return G1, G2


def wfs1(G, start):
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


def check(G, i):
    used = set()
    used.add(i)

    from collections import deque
    d = deque()
    d.append(i)

    while (len(d)):
        v = d.popleft()
        for neigh in G[v]:
            if neigh in used:
                continue
            else:
                d.append(neigh)
                used.add(neigh)
    return len(used)


N, M = map(int, input().split())
G1, G2 = create_Graph(M)

for i in range(1, N + 1):
    if check(G1, i) == N or check(G2, i):
        break
else:
    print("No")
    quit()

for start in G1.keys():
    arr = wfs1(G1, start)
    for x in arr:
        if len(x) == 0:
            continue
        else:
            print("No")
            quit()

print("Yes")
