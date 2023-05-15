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


def find_leaves(t):
    if t is None:
        return
    if t["right"] is None and t["left"] is None:
        leaves.append(t["value"])
        return
    find_leaves(t["right"])
    find_leaves(t["left"])


a = BinTree()
leaves = []
overall_height = 0
num = list(map(int, input().split()))
for i in range(len(num)):
    insert_into_tree(a, num[i])

find_leaves(a["root"])
print(" ".join(map(str, sorted(leaves))))
