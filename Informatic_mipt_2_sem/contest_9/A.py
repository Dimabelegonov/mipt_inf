n = int(input())
edges = []
for i in range(n):
    d = list(map(int, input().split()))
    for j in range(n):
        if d[j] == 1 and i < j:
            edges.append([i, j])

t = input()
colors = list(map(int, input().split()))
ans = 0
for e in edges:
    if colors[e[0]] != colors[e[1]]:
        ans += 1

print(ans)
