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
    num = -1
    minlen = float("+inf")
    for i in range(len(G)):
        sum = 0
        for x in G[i]:
            sum += x
        if sum < minlen:
            minlen = sum
            num = i
    print(num)


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
