def check(G):
    ne_istok = set()
    stok = set()
    istok = {a for a in range(1, len(G) + 1)}
    for i in range(len(G)):
        marker = True
        for j in range(len(G[i])):
            if G[i][j] == 0:
                continue
            else:
                ne_istok.add(j + 1)
                marker = False
        if marker:
            stok.add(i + 1)

    print(*sorted(istok - ne_istok))
    print(*sorted(stok))


N = int(input())
Matrix = []
for _ in range(N):
    Matrix.append(list(map(int, input().split())))
check(Matrix)
