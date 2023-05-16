def input_graph(n, m):
    adj_list = [dict() for i in range(n)]
    for i in range(m):
        node_1, node_2, dist = map(int, input().split())
        adj_list[node_1][node_2] = dist
        adj_list[node_2][node_1] = dist
    return adj_list


def min_index(arr, excluded_set):
    min_v = float("inf")
    min_i = -1

    for i in range(len(arr)):
        if i not in excluded_set and arr[i] < min_v:
            min_i = i
            min_v = arr[i]

    return min_i


def prim(adj_list):
    distances = [0 if i == 0 else float("inf") for i in range(len(adj_list))]
    origin = [None for i in range(len(adj_list))]
    reached = set()
    tree_weight = 0
    tree_edges = []

    for i in range(len(adj_list)):
        curr_node = min_index(distances, reached)
        reached.add(curr_node)
        tree_edges.append((origin[curr_node], curr_node))
        tree_weight += distances[curr_node]

        for adj_node in adj_list[curr_node]:
            if adj_list[curr_node][adj_node] < distances[adj_node]:
                distances[adj_node] = adj_list[curr_node][adj_node]
                origin[adj_node] = curr_node

    return tree_weight, tree_edges[1:]


def solve_task():
    n, m = map(int, input().split())
    adj_list = input_graph(n, m)
    weight, edges = prim(adj_list)
    print(weight)
    for edge in edges:
        print(*edge)


solve_task()
