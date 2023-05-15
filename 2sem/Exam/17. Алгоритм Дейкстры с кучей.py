"""
Находит кратчайшие пути от одной из вершин графа до всех остальных.
Алгоритм работает только для графов без рёбер отрицательного веса.

Видос - https://youtu.be/d2p60l9r-YY?t=439

O(N^2) - для тупого способа (!=16 билет)
0(N*log2(M)+N*log2(M)) - для крутого способа
"""
import heapq


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


def deikstra(G, start, N):
    heap = []
    used = set()
    used.add(start)

    table = [float("inf")] * N
    table[start] = 0
    heapq.heappush(heap, (0, start))

    while len(heap):
        v = heapq.heappop(heap)[1]
        for neigh in G[v]:
            if table[neigh] > G[v][neigh] + table[v]:
                table[neigh] = G[v][neigh] + table[v]
                heapq.heappush(heap, (table[neigh], neigh))
    print(table)


N, M = map(int, input().split())
G = create_Graph(M)
deikstra(G, int(input("Start-Vertex:")), N)

"""
Пример ввода:
4 5
0 2 1
2 1 3
2 3 6
1 3 2
0 3 15
"""
