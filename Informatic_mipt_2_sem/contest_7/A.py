queue = []
n, m, x, y = map(int, input().split())
used = [False for _ in range(n)]
d = [0 for _ in range(n)]
p = [0 for _ in range(n)]
edge = {}
for _ in range(m):
    a, b = map(int, input().split())
    if a in edge.keys():
        edge[a].append(b)
    else:
        edge[a] = [b]

    if b in edge.keys():
        edge[b].append(a)
    else:
        edge[b] = [a]


queue.append(x)
used[x] = True
p[x] = -1
while len(queue) > 0:
    v = queue.pop(0)
    for new_v in edge[v]:
        if not used[new_v]:
            used[new_v] = True
            queue.append(new_v)
            d[new_v] = d[v] + 1
            p[new_v] = v


# print(d)
print(d[y])
# print(p)

