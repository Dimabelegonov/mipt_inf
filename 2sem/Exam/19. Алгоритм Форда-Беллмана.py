"""
Алгоритм Форда-Беллмана позволяет найти кратчайшие пути из одной
вершины графа до всех остальных, даже для графов, в которых веса
ребер могут быть отрицательными. Тем не менее, в графе не должно
быть циклов отрицательного веса, достижимых из начальной вершины,
иначе вопрос о кратчайших путях является бессмысленным.

Видос - https://youtu.be/d2p60l9r-YY?t=2634

Если сделать N+1 шаг, то изменятся расстояния только у вершин, которые входят в отрицательный цикл.

Работает, что с ориентированным, что с неориентированным графом

O(N*M)
"""


def create_Edges(M):
    Edges = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        Edges.append((a, b, c))
        Edges.append((b, a, c))
    return Edges


def ford_bellman(Edges, N, start):
    table = [[float("+inf")] * N for _ in range(N)]
    for i in range(N):
        table[i][start] = 0

    for i in range(1, N):
        for x, y, w in Edges:
            table[i][y] = min(table[i][y], table[i - 1][y], table[i - 1][x] + w)

    for i in range(len(table)):
        print("N" + str(i), " ".join(map(str, table[i])))


N, M = map(int, input().split())
Edges = create_Edges(M)
ford_bellman(Edges, N, int(input("Start-Vertex:")))

"""
Пример ввода: 
5 4
0 2 3
2 3 6
3 4 7
4 1 2
"""
