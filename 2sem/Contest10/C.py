from collections import deque


def add_to_G(G):
    a, b = map(int, input().split())
    for v in (a, b):
        if v not in G:
            G[v] = []
    G[a].append(b)
    G[b].append(a)

    return a, b


def check1(G, i):
    used = set()
    used.add(i)

    d = deque()
    d.append(i)

    while (len(d)):
        v = d.popleft()
        for neigh in G[v]:
            if neigh in used:
                continue
            else:
                d.append(neigh)
                used.add(neigh)
    return used


def check2(G, i, used):
    d = deque()
    d.append(i)

    while (len(d)):
        v = d.popleft()
        for neigh in G[v]:
            if neigh in used:
                continue
            else:
                d.append(neigh)
                used.add(neigh)
    return len(used)


N, M = map(int, input().split())
G = {}
used = set()
for i in range(M):
    a, b = add_to_G(G)
    if a in used and b in used:
        continue
    if a not in used and b not in used:
        el = a
        used = check1(G, el)
        if len(used) == N:
            print(i + 1)
            break
        else:
            continue
    elif a not in used:
        used.add(a)
        if check2(G, a, used) == N:
            print(i + 1)
            break
    elif b not in used:
        used.add(b)
        if check2(G, b, used) == N:
            print(i + 1)
            break
