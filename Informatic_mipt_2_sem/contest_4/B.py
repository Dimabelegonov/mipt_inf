class Node():
    def __init__(self, val, n):
        self.value = val
        self.right = None
        self.left = None
        self.n = n


def add_node(node: Node, main_node: Node):
    global ans

    if main_node.value >= node.value:
        if main_node.right is None:
            main_node.right = node
            node.n = main_node.n + 1
            ans = max(ans, node.n)
        else:
            add_node(node, main_node.right)
    else:
        if main_node.left is None:
            main_node.left = node
            node.n = main_node.n + 1
            ans = max(ans, node.n)
        else:
            add_node(node, main_node.left)


nodes = []
data = list(map(int, input().split()))
ans = 0
if len(data) > 0:
    nodes.append(Node(data[0], 1))
    ans = 1
    for a in data[1::]:
        node = Node(a, 1)
        nodes.append(node)
        add_node(node, nodes[0])
    print(ans)
else:
    print(ans)