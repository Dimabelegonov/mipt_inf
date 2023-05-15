def create_Edges(M):
    Edges = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        Edges.append((a, b, c))
    return Edges


def Ford_Bellman(n, edges_list, start_node):
    distances = [0 if i == start_node else float("inf") for i in range(n)]
    for i in range(n - 1):
        condition_passed = False
        for first_node, second_node, dist in edges_list:
            if distances[first_node] + dist < distances[second_node]:
                distances[second_node] = distances[first_node] + dist
                condition_passed = True
        if not condition_passed:
            break
    undefined_set = set()
    for i in range(n):
        condition_passed = False
        for first_node, second_node, dist in edges_list:
            if distances[first_node] + dist < distances[second_node]:
                distances[second_node] = distances[first_node] + dist
                undefined_set.add(second_node)
                condition_passed = True
        if not condition_passed:
            break
    for node in range(n):
        if node in undefined_set or distances[node] == float("inf"):
            distances[node] = "UDF"
    return distances


N, M, S = map(int, input().split())
Edges = create_Edges(M)
print(" ".join(map(str, Ford_Bellman(N, Edges, S))))
