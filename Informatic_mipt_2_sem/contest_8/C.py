class Graph():
    def __init__(self, n, graph):
        self.n = n
        self.matrix = graph
        self.min_distance = [0, inf]

    def get_min_vert(self):
        min_dist = [0, inf]
        for v in range(self.n):
            if self.used[v] and min_dist[1] > self.dist[v]:
                min_dist[0] = v
                min_dist[1] = self.dist[v]

        return min_dist[0]

    def check_min_distance(self, ind):
        sum_ = sum(self.dist)
        if self.min_distance[1] > sum_:
            self.min_distance[0] = ind
            self.min_distance[1] = sum_

    def dijkstra(self, start):
        self.dist = [inf for _ in range(self.n)]
        self.used = [True for _ in range(self.n)]
        self.dist[start] = 0

        for _ in range(self.n):
            # print(self.dist)
            v = self.get_min_vert()
            # print(v)
            self.used[v] = False
            for t in range(n):
                if self.used[t]:
                    self.dist[t] = min(self.dist[t], self.dist[v] + self.matrix[v][t])

        self.check_min_distance(start)



inf = 10 ** 9
n, m = (int(s) for s in input().split())

graph = [[inf] * n for _ in range(n)]

for i in range(m):
    c1, c2, distance = (int(s) for s in input().split())
    graph[c1][c2] = distance
    graph[c2][c1] = distance

g = Graph(n, graph)

for i in range(n):
    g.dijkstra(i)
    # print(g.min_distance)

print(g.min_distance[0])
