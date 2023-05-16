sets = {}


def make_set(name):
    sets[name] = {
        "parent": name,
        "count": 1
    }


def find_set(name):
    if name == sets[name]["parent"]:
        return name

    sets[name]["parent"] = find_set(sets[name]["parent"])
    return sets[name]["parent"]


def union_set(name1, name2):
    name1 = find_set(name1)
    name2 = find_set(name2)

    if name1 != name2:
        if sets[name1]["count"] < sets[name2]["count"]:
            name1, name2 = name2, name1

        sets[name2]["parent"] = sets[name1]["parent"]
        sets[name1]["count"] += sets[name2]["count"]


def main():
    n, m = map(int, input().split())
    for i in range(n):
        make_set(i)

    # print(sets)
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))

    count = n - 1
    answer = 0
    for v1, v2 in edges:
        v1, v2 = map(find_set, (v1, v2))
        answer += 1
        if v1 != v2:
            union_set(v1, v2)
            count -= 1
            if count == 0:
                return answer

        # print(sets)

print(main())