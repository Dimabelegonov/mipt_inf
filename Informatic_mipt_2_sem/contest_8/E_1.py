def add_edge(graph, v1, v2, weight):
    if v1 not in graph:
        graph[v1] = {v2: weight}
    else:
        graph[v1][v2] = weight


def create_graph():
    for _ in range(size):
        v1, v2, weight = map(int, input().split())
        add_edge(graph, v1, v2, weight)
        add_edge(graph, v2, v1, weight)


def dijkstra(graph, start, distances):
    queue = deque([start])
    while queue:
        cur_v = queue.popleft()
        for neigh_v in graph[cur_v]:
            if neigh_v not in distances:
                distances[neigh_v] = [start, distances[cur_v][1] + graph[cur_v][neigh_v]]
                queue.append(neigh_v)

            elif (distances[neigh_v][0] > distances[cur_v][0] + graph[cur_v][neigh_v]):
                distances[neigh_v][0] = start
                distances[neigh_v][1] = distances[cur_v][1] + graph[cur_v][neigh_v]
                queue.append(neigh_v)

from collections import deque

centeres = list(map(int, input().split()))
order = centeres.pop(0)
size = centeres.pop(0)

graph = dict()
create_graph()

distances = dict()
for center in centeres:
    distances[center] = [center, 0]

for center in centeres:
    dijkstra(graph, center, distances)

for vertex in range(order):
    if vertex in distances:
        print(distances[vertex][0])
    else:
        print(-1)