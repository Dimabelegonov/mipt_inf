from collections import deque


class Graph():
    def __init__(self, n, graph):
        self.n = n
        self.matrix = graph

    def get_way(self, start, end):
        if end not in self.dist.keys():
            return [-1]

        way = [end[0]]
        while end != start:
            new_v = self.parent[end]
            way.append(new_v[0])
            end = new_v
        return way[::-1]

    def dijkstra(self, start):
        self.dist = {}
        self.parent = {}
        self.dist[start] = 0
        queue = deque([start])

        while queue:
            # print(self.dist)
            cur_v = queue.popleft()
            # print(v)
            # self.used[v] = False
            for neigh_v in self.matrix[cur_v]:
                if (neigh_v not in self.dist or
                    self.dist[cur_v] + self.matrix[cur_v][neigh_v] < self.dist[neigh_v]):
                    self.dist[neigh_v] = self.dist[cur_v] + self.matrix[cur_v][neigh_v]
                    self.parent[neigh_v] = cur_v
                    queue.append(neigh_v)


def add_edge(graph, v1, v2, weight):
    if (v1, 0) not in graph:
        graph[(v1, 0)] = {(v2, 1): weight}
        graph[(v1, 1)] = {(v2, 2): weight}
        graph[(v1, 2)] = {(v2, 0): weight}
    else:
        graph[(v1, 0)][(v2, 1)] = weight
        graph[(v1, 1)][(v2, 2)] = weight
        graph[(v1, 2)][(v2, 0)] = weight


n, m = map(int, input().split())
inf = 10 ** 9
edges = {}
for _ in range(m):
    v1, v2, w = map(int, input().split())
    add_edge(edges, v1, v2, w)
    add_edge(edges, v2, v1, w)


graphs = [-1 for _ in range(n)]

k = int(input())
for t in range(k):
    start, end = map(int, input().split())
    if graphs[start] == -1:
        graphs[start] = Graph(2 * n, edges)
        graphs[start].dijkstra((start, 0))
    print(*graphs[start].get_way((start, 0), (end, 1)))
