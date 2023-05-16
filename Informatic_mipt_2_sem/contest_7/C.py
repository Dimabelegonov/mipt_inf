from collections import deque


n, m = map(int, input().split())
edge = {v: [] for v in range(n)}
data = []
for _ in range(m):
    a, b = map(int, input().split())
    edge[a].append(b)


def bfs(edge, start):
    global data
    parent = {v: None for v in range(n)}
    dist = {v: [] for v in range(n)}

    q = deque()
    q.append(start)
    parent[start] = -1

    while len(q) != 0:
        v = q.pop()
        for neighbour in edge[v]:
            if parent[neighbour] is None:
                q.append(neighbour)
                parent[neighbour] = v
                dist[neighbour] = dist[v] + [v]
            elif parent[v] != neighbour:
                if neighbour in dist.keys() and v in dist.keys():
                    if len(dist[neighbour]) == 0:
                        a = dist[v] + [v]
                        if len(data) == 0:
                            data = list(a)
                        elif len(data) > len(a):
                            data = list(a)


def main():
    for s in range(n):
        bfs(edge, s)

    # print(data)
    if len(data) > 0:
        print(*data)
    else:
        print("NO CYCLES")

main()