"""
Списки (или множества) смежных вершин. - круто add/del, но не круто хранить
Если перевести буквы в числа - будет быстрее.
"""


def create_Graph1(N, M):
    G = {}
    for _ in range(M):
        a, b = map(int, input().split())
        for v in (a, b):
            if v not in G:
                G[v] = []
        G[a].append(b)

    print(G)


"""
Матрица смежности. - круто add/del, но не круто хранить
"""


def create_Graph2(N):
    G = [[0] * N for _ in range(N)]
    V_names = []

    for _ in range():
        a, b = map(int, input().split())
        for v in (a, b):
            if v not in V_names:
                V_names.append(v)
        i1 = V_names.index(a)
        i2 = V_names.index(b)

        G[i1][i2], G[i2][i1] = 1, 1

    for i in range(len(G)):
        print(" ".join(map(str, G[i])))

    for V_ind, V_name in enumerate(V_names):
        print(
            V_name,
            G[V_ind].count(1),
            *[v for i, v in enumerate(V_names) if G[V_ind][i] == 1]
        )


"""
Компактный способ хранения данных.
offset - сдвиг
"""


def create_Graph3(G):
    offset = [0]
    edges = []

    for i in G:
        for e in i:
            edges.append(e)
        offset.append(len(edges))

    for vi in range(len(offset) - 1):
        print(
            vi,
            offset[vi + 1] - offset[vi],
            *edges[offset[vi]:offset[vi + 1]]
        )
