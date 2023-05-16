n, m = map(int, input().split())
edge = {}
queue = []
used = [False for _ in range(n)]
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


queue.append(0)
used[0] = True
answer = []
while len(queue) > 0:
    v = queue.pop(0)
    for new_v in edge[v]:
        if not used[new_v]:
            used[new_v] = True
            queue.append(new_v)
            answer.append((v, new_v))


for t in answer:
    print(*t)