def main():
    n = int(input())
    p = int(input())
    data = {}
    color = [0 for i in range(n)]
    for i in range(p):
        a, b = map(int, input().split())
        if a in data.keys():
            data[a].append(b)
        else:
            data[a] = [b]
    for v in range(n):
        dfs(v, data, color)
        for g in color:
            if g == 0:
                return False
        color = [0 for i in range(n)]

    return True

def dfs(v, graph, color):
    color[v] = 1
    if v in graph.keys():
        for t in graph[v]:
            if color[t] == 0:
                dfs(t, graph, color)


if main():
    print("YES")
else:
    print("NO")

