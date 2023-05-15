def BinTree():
    return {"root": None}


def Node(value):
    return {"value": value, "left": None, "right": None}


def insert_into_tree(t, value):
    if t["root"] is None:
        t["root"] = Node(value)
    else:
        insert_into_Node(t["root"], value)


def insert_into_Node(node, value):
    if value == node["value"]:
        return
    if node["value"] > value:
        if node["left"] is None:
            node["left"] = Node(value)
        else:
            insert_into_Node(node["left"], value)

    elif node["value"] < value:
        if node["right"] is None:
            node["right"] = Node(value)
        else:
            insert_into_Node(node["right"], value)


def tree_height(t):
    if t is None:
        return 0

    return max(tree_height(t["right"]), tree_height(t["left"])) + 1


a = BinTree()
overall_height = 0
num = list(map(int, input().split()))
for i in range(len(num)):
    insert_into_tree(a, num[i])
print(tree_height(a["root"]))
