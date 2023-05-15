def traversal(node):
    if node[1] != -1:
        traversal(nodes[node[1]])

    new.append(node[0])

    if node[2] != -1:
        traversal(nodes[node[2]])


N = int(input())
nodes = []
new = []
for i in range(N):
    a = list(map(int, input().split()))
    nodes.append([a[0], a[1], a[2]])

traversal(nodes[0])

if new == sorted(new):
    print("YES")
else:
    print("NO")
