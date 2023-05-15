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


def dfs(G, vertex, used, componenta):
    used.add(vertex)
    for v in G[vertex]:
        if v not in used:
            dfs(G, v, used, componenta)
    componenta.append(vertex)


N, M = int(input()), int(input())
G = create_Graph(M)

used = set()
comp = []
for vertex in G.keys():
    if vertex not in used:
        componenta = []
        dfs(G, vertex, used, componenta)
        print(componenta)
