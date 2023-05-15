def print_edge(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] != 0:
                print(i, j, a[i][j])
    return 0


N = int(input())
a = []
for _ in range(N):
    a.append(list(map(int, input().split())))

print_edge(a)
