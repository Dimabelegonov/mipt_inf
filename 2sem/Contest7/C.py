"""
Словами - https://youtu.be/8x5JQMAXtOg
"""


def create_Graph(M):
    G = {}
    G_inv = {}
    for _ in range(M):
        a, b = map(int, input().split())
        for v in (a, b):
            if v not in G:
                G[v] = []
                G_inv[v] = []

        G[a].append(b)
        G_inv[b].append(a)

    return G, G_inv


def dfs(G, vertex, used, stack):
    used.add(vertex)
    for v in G[vertex]:
        if v not in used:
            dfs(G, v, used, stack)
    stack.append(vertex)


N, M = int(input()), int(input())
G, G_inv = create_Graph(M)

used = set()
stack = []
for vertex in G.keys():
    if vertex not in used:
        dfs(G, vertex, used, stack)

cnt = 0
used = set()
while len(stack) > 0:
    v = stack.pop()
    if v not in used:
        componenta = []
        dfs(G_inv, v, used, componenta)
        cnt += 1

if cnt == 1:
    print("YES")
else:
    print("NO")
