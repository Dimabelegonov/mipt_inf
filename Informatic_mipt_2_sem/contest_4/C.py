class Node():
    def __init__(self, val):
        self.value = val
        self.right = None
        self.left = None


def add_node(node: Node, main_node: Node):
    if main_node.value >= node.value:
        if main_node.right is None:
            main_node.right = node
        else:
            add_node(node, main_node.right)
    else:
        if main_node.left is None:
            main_node.left = node
        else:
            add_node(node, main_node.left)


nodes = []
data = list(map(int, input().split()))
ans = []
if len(data) > 0:
    nodes.append(Node(data[0]))
    for a in data[1::]:
        node = Node(a)
        nodes.append(node)
        add_node(node, nodes[0])

    for a in nodes:
        if a.right == a.left == None:
            ans.append(a.value)

    print(*sorted(ans))
else:
    print(ans)