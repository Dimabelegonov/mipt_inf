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
    marker[vertex] = 1
    if vertex in G.keys():
        for v in G[vertex]:
            if marker[v] == 1:
                return [v, vertex]
            elif marker[v] == 0:
                ans = dfs(G, v, marker)
                if ans:
                    return ans + [vertex]
    marker[vertex] = 2
    return False


N, M = map(int, input().split())
G = create_Graph(M)

for v in G.keys():
    marker = [0] * N
    ans = dfs(G, v, marker)
    if ans:
        res = [ans[0]]
        for i in range(1, len(ans)):
            if ans[i] != ans[0]:
                res.append(ans[i])
            else:
                break
        else:
            continue
        end = res[1:]
        print(res[0], " ".join(map(str, end[::-1])))
        quit()
print("No cycles")
