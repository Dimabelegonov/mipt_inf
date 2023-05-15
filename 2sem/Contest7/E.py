def create_Graph(M):
    G = {}
    for _ in range(M):
        a, b = map(int, input().split())
        if a not in G:
            G[a] = [b]
        else:
            G[a].append(b)

    return G


def dfs(G, vertex, marker):
    global ans
    marker[vertex] = 1
    if vertex in G.keys():
        for v in G[vertex]:
            if marker[v] == 0:
                t = dfs(G, v, marker)
                if not t:
                    return False
            elif marker[v] == 1:
                return False

    ans.append(vertex)
    marker[vertex] = 2
    return True


N, M = map(int, input().split())
G = create_Graph(M)
marker = [0] * N
ans = []

for v in range(N):
    if marker[v] == 0:
        t = dfs(G, v, marker)
        if not t:
            print("NO")
            quit()
print(" ".join(map(str, ans[::-1])))
