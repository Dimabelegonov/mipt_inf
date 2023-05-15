"""
Алгоритм поиска минимального остовного дерева во взвешенном неориентированном/ориентированном связном графе.
Видос1 - https://youtu.be/W_fFmZjWzk8?t=4018
Видос2 - https://youtu.be/W_fFmZjWzk8?t=4018

O(M * logM + M * x), где x < logM (благодаря системе непересекающихся множеств)
"""

vertex_sets = {}


def make_set(x):
    return {
        "parent": x,
        "count": 1
    }


def find_set(x):
    if vertex_sets[x]["parent"] == x:
        return x
    else:
        # Сразу указать изначальную вершину (так быстрее)
        y = find_set(vertex_sets[x]["parent"])
        vertex_sets[x]["parent"] = y
        return y


def union_set(x, y):
    x, y = map(find_set, (x, y))
    if vertex_sets[x]["count"] < vertex_sets[y]["count"]:
        x, y = y, x
    vertex_sets[y]["parent"] = x
    vertex_sets[x]["count"] += vertex_sets[y]["count"]


E = []
N, M = map(int, input().split())
for _ in range(M):
    x, y, w, = map(int, input().split())
    vertex_sets[x] = make_set(x)
    vertex_sets[y] = make_set(y)
    E.append((x, y, w))

E.sort(key=lambda x: x[2])

min_tree = []
min_weight = 0

for x, y, w in E:
    if find_set(x) != find_set(y):
        min_weight += w
        min_tree.append((x, y, w))
        union_set(x, y)
print(min_weight, min_tree, vertex_sets, sep="\n")

"""
Пример ввода:
7 11
0 1 7
0 3 5
3 1 9
1 2 8
1 4 7
2 4 5
3 4 15
3 5 6
5 4 8
5 6 11
6 4 9
"""
