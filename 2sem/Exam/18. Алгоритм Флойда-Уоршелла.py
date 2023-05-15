"""
Алгоритм Флойда–Уоршелла — алгоритм нахождения длин кратчайших путей
между всеми парами вершин во взвешенном графе.
Работает корректно, если в графе нет циклов отрицательной величины,
а в случае, когда такой цикл есть, позволяет найти хотя бы один такой цикл.

Видео - https://youtu.be/d2p60l9r-YY?t=3391
O(N^3) В какие-то моменты может быть быстрее Дейкстеры для всех вершин.
"""


def create_Graph(N, M):
    G = [[float("+inf") if i != j else 0 for j in range(N)] for i in range(N)]
    for i in range(M):
        a, b, c = map(int, input().split())
        G[a][b] = c
        G[b][a] = c

    return G


def floyd_warshall(G):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                G[i][j] = min(G[i][j], G[i][k] + G[k][j])
    for line in G:
        print(" ".join(map(str, line)))


N, M = map(int, input().split())
G = create_Graph(N, M)
floyd_warshall(G)

"""
Пример ввода: 
5 4
1 2 3
2 3 6
3 4 7
4 1 2
"""
