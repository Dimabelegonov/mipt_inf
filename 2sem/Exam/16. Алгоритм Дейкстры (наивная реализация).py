"""
Находит кратчайшие пути от одной из вершин графа до всех остальных.
Алгоритм работает только для графов без рёбер отрицательного веса.

Видос - https://youtu.be/d2p60l9r-YY?t=136

O(N^2)
"""


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
    print(" ".join(map(str, table)))


N, M = map(int, input().split())
G = create_Graph(M)
dfs(G, int(input("Start-Vertex:")), N)

"""
Пример ввода:
4 5
0 2 1
2 1 3
2 3 6
1 3 2
0 3 15
"""
