def generate_arr(node):
    if node[1] != -1:
        generate_arr(nodes[node[1]])

    data.append(node[0])

    if node[2] != -1:
        generate_arr(nodes[node[2]])

n = int(input())
nodes = []
data = []

for _ in range(n):
    value, left, right = [int(val) for val in input().split()]
    nodes.append([value, left, right])


generate_arr(nodes[0])
if data == sorted(data):
    print("YES")
else:
    print("NO")
