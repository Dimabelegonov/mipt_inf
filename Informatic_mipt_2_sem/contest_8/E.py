from collections import deque


class Graph():
    def __init__(self, n, graph):
        self.n = n
        self.matrix = graph
        self.dist = {}

    def dijkstra(self, start):
        self.dist[start] = [start, 0]
        queue = deque([start])

        while queue:
            # print(self.dist)
            cur_v = queue.popleft()
            # print(v)
            # self.used[v] = False
            for neigh_v in self.matrix[cur_v]:
                if neigh_v not in self.dist:
                    self.dist[neigh_v] = [start, self.dist[cur_v][1] + self.matrix[cur_v][neigh_v]]
                    queue.append(neigh_v)
                elif self.dist[neigh_v][1] > self.dist[cur_v][1] + self.matrix[cur_v][neigh_v]:
                    self.dist[neigh_v][0] = start
                    self.dist[neigh_v][1] = self.dist[cur_v][1] + self.matrix[cur_v][neigh_v]
                    queue.append(neigh_v)


def add_edge(graph, v1, v2, w):
    if v1 not in graph:
        graph[v1] = {v2: w}
    else:
        graph[v1][v2] = w


def main():
    data = list(map(int, input().split()))
    n, m = data[0], data[1]
    main_cities = data[2::]
    inf = 10 ** 9
    graph = {}
    for _ in range(m):
        v1, v2, w = map(int, input().split())
        add_edge(graph, v1, v2, w)
        add_edge(graph, v2, v1, w)

    g = Graph(n, graph)
    for c in main_cities:
        g.dijkstra(c)

    # print(g.dist)

    for v in range(n):
        if v in g.dist:
            print(g.dist[v][0])
        else:
            print(-1)


main()
