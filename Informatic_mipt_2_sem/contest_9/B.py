def dfs(graph: dict, v: int, color: list):
    global ans
    color[v] = 1
    if v in graph.keys():
        for f in graph[v]:
            if color[f] == 0:
                t = dfs(graph, f, color)
                if not t:
                    return False
            elif color[f] == 1:
                return False

    ans.append(v)
    color[v] = 2
    return True

def main():
    n, m = map(int, input().split())
    data = {}
    for _ in range(m):
        a, b = map(int, input().split())
        if a in data.keys():
            data[a].append(b)
        else:
            data[a] = [b]
    color = [0 for i in range(n + 1)]
    for v in range(1, n + 1):
        if color[v] == 0:
            t = dfs(data, v, color)
            if not t:
                return False
    return True


ans = []
if main():
    print("Yes")
else:
    print("No")
