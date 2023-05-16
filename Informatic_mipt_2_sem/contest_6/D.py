def dfs(graph: dict, v: int, color: list):
    color[v] = 1
    if v in graph.keys():
        for f in graph[v]:
            if color[f] == 1:
                return [f, v]
            elif color[f] == 0:
                ans = dfs(graph, f, color)
                if ans:
                    return ans + [v]

    color[v] = 2
    return False


def main():
    n, m = map(int, input().split())
    data = {}
    for _ in range(m):
        a, b = map(int, input().split())
        if a in data.keys():
            data[a].append(b)
        else:
            data[a] = [b]
    for v in range(1, n + 1):
        color = [0 for i in range(n + 1)]
        ans = dfs(data, v, color)
        if ans:
            answer = [ans[0]]
            for g in range(1, len(ans)):
                if ans[g] == ans[0]:
                    break
                else:
                    answer.append(ans[g])
            return " ".join(map(str, answer[::-1]))

    return "YES"


print(main())
