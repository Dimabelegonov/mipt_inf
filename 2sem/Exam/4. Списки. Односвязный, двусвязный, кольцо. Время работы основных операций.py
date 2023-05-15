"""
Связный список — базовая динамическая структура данных в информатике,
состоящая из узлов, содержащих данные и ссылки («связки») на следующий
и/или предыдущий узел списка. Принципиальным преимуществом перед массивом
является структурная гибкость: порядок элементов связного списка может не
совпадать с порядком расположения элементов данных в памяти компьютера,
а порядок обхода списка всегда явно задаётся его внутренними связями.

Проблемы обычных списков:
1)Удалять
2)Добавлять

Все операции O(1)

Видос - https://youtu.be/VwJKzE0jfz4?t=710
"""

"""
Односвязный
"""


def linkedlist():
    return {"first": None}


def Node(value):
    return {"value": value, "next": None}


def add_to_list(value, llist):
    new_node = Node(value)
    new_node["next"] = llist["first"]
    llist["first"] = new_node


def pop_from_list(llist):
    res = llist["first"]["value"]
    llist["first"] = llist["first"]["next"]
    return res


def print_list(llist):
    current = llist["first"]
    while current != None:
        print(current["value"], end=" ")
        current = current["next"]


def insert_value(node, value):
    new_node = Node(value)
    new_node["next"] = node["next"]
    node["next"] = new_node


llist = linkedlist()
for _ in range(5):
    add_to_list(int(input()), llist)
print(llist)
print(pop_from_list(llist))
print_list(llist)

"""
Двусвязный
"""


def linkedlist():
    return {"first": None}


def Node(value):
    return {"value": value, "next": None, "prev": None}


def add_to_list(value, llist):
    if llist["first"] == None:
        new_node = Node(value)
        new_node["next"] = llist["first"]
        llist["first"] = new_node
    else:
        new_node = Node(value)
        llist["first"]["prev"] = value
        new_node["next"] = llist["first"]
        llist["first"] = new_node


def pop_from_list(llist):
    res = llist["first"]["value"]
    llist["first"] = llist["first"]["next"]
    llist["first"]["prev"] = None
    return res


def print_list(llist):
    current = llist["first"]
    while current != None:
        print(current["value"], end=" ")
        current = current["next"]


def insert_value(node, value):
    new_node = Node(value)
    new_node["next"] = node["next"]
    new_node["next"]["prev"] = value
    new_node["prev"] = node["prev"]
    node["next"] = new_node


llist = linkedlist()
for _ in range(5):
    add_to_list(int(input()), llist)
print(llist)
print(pop_from_list(llist))
print(llist)
print_list(llist)

"""
Кольцо
Всё аналогично только теперь есть last у которого next это first
"""


def linkedlist():
    return {"first": None}
