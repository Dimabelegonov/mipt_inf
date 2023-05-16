def input_graph(N, M):
    adj_list = [set() for i in range(N)]
    rev_adj_list = [set() for i in range(N)]
    for i in range(M):
        first_node, second_node = map(int, input().split())
        adj_list[first_node].add(second_node)
        rev_adj_list[second_node].add(first_node)
    return adj_list, rev_adj_list


def game(curr_node, rev_adj_list, edges_counter, victory_set, defeat_set):
    for origin_node in rev_adj_list[curr_node]:
        if origin_node not in victory_set and origin_node not in defeat_set:
            if curr_node in defeat_set:
                victory_set.add(origin_node)
                game(origin_node, rev_adj_list, edges_counter, victory_set, defeat_set)
            elif curr_node in victory_set:
                edges_counter[origin_node] -= 1
                if edges_counter[origin_node] == 0:
                    defeat_set.add(origin_node)
                    game(origin_node, rev_adj_list, edges_counter, victory_set, defeat_set)


def solve():
    N, M, K = map(int, input().split())
    adj_list, rev_adj_list = input_graph(N, M)
    victory_set = set()
    defeat_set = set()
    for node in range(N):
        if len(adj_list[node]) == 0:
            defeat_set.add(node)
    edges_counter = [len(adj_list[node]) for node in range(N)]
    start_set = {node for node in defeat_set}
    for defeat_node in start_set:
        game(defeat_node, rev_adj_list, edges_counter, victory_set, defeat_set)

    if K in victory_set:
        print("Win")
    elif K in defeat_set:
        print("Lose")
    else:
        print("Draw")


solve()
