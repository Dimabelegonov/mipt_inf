"""
Двудольный граф - граф, вершины которого можно разбить на два множества так,
что каждое ребро соединяет вершины из разных множеств.
"""


def create_Graph(M):
    G = {}
    for _ in range(M):
        a, b = map(int, input().split())
        if a not in G:
            G[a] = [b]
        else:
            G[a].append(b)
    return G


def wfs(G, vertex, used, marker):
    from collections import deque
    d = deque()
    d.append(vertex)
    marker[vertex] = 1

    while (len(d)):
        v = d.popleft()
        if v not in used:
            used.add(v)
            for neigh in G[v]:
                if neigh not in used:
                    marker[neigh] = 2 / marker[v]
                    used.add(neigh)
                    d.append(neigh)
                else:
                    if marker[neigh] * marker[v] != 2:
                        print("NO")
                        quit()


N, M = int(input()), int(input())
G = create_Graph(M)

used = set()
marker = [0] * N
for vertex in G.keys():
    if vertex not in used:
        wfs(G, vertex, used, marker)
print("YES")
