"""
Алгоритм построения минимального остовного дерева взвешенного связного неориентированного графа.
Видос - https://youtu.be/W_fFmZjWzk8?t=97

O(N^2) + есть способ O(N*M) - о нём говорят в видосе, но он геморный
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


def prim(G, N, start):
    distance = [float("inf")] * N
    distance[start] = 0

    paths = [0] * N
    paths[start] = start

    way = []
    used = set()
    v = start

    for _ in range(N):
        used.add(v)
        for h in G[v]:
            if G[v][h] < distance[h] and h not in used:
                distance[h] = G[v][h]
                paths[h] = v

        mint = float("inf")
        for i in range(N):
            if i not in used and distance[i] < mint:
                mint = distance[i]
                num = i
        way.append((paths[num], num))
        v = num

    print(" ".join(map(str, distance)), " - таблица расстояний")
    print(" ".join(map(str, way)), " - путь")
    print(sum(distance), " - длина пути")


N, M = map(int, input().split())
G = create_Graph(M)

prim(G, N, int(input("Start Vertex:")))

"""
Пример ввода:
7 11
0 1 7
0 3 5
3 1 9
1 2 8
1 4 7
2 4 5
3 4 15
3 5 6
5 4 8
5 6 11
6 4 9
"""
