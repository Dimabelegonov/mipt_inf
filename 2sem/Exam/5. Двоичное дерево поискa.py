"""
Двоичное дерево поиска  — двоичное дерево, для которого выполняются
следующие дополнительные условия:

1)Оба поддерева — левое и правое — являются двоичными деревьями поиска.

2)У всех узлов левого поддерева произвольного узла X значения ключей
данных меньше либо равны, нежели значение ключа данных самого узла X.

3)У всех узлов правого поддерева произвольного узла X значения ключей
данных больше, нежели значение ключа данных самого узла X.

abs(hl-hr)<=1 - сбалансированное дерево
"""

"""
Плюсы:

1)При правильном чтении - получаем отсортированный массив данных.

2)Быстрый поиск элементов.
"""

"""
Реализация добавления элементов в дерево:
"""


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


a = BinTree()
num = list(map(int, input().split()))
for i in range(len(num)):
    insert_into_tree(a, num[i])
print(a)
