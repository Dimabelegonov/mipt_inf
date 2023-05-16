n, m = map(int, input().split())
data = []
f_queue = []
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(m):
        if a[j] == 1:
            f_queue.append((i, j))
        else:
            a[j] = -1
    data.append(a)


d = 0
sec_queue = []
while len(f_queue) > 0:
    for x, y in f_queue:
        if d < data[x][y] or data[x][y] == -1:
            data[x][y] = d
            if x + 1 < n:
                sec_queue.append((x + 1, y))
            if x - 1 >= 0:
                sec_queue.append((x - 1, y))
            if y + 1 < m:
                sec_queue.append((x, y + 1))
            if y - 1 >= 0:
                sec_queue.append((x, y - 1))

    f_queue = list(sec_queue)
    sec_queue = []
    d += 1


for x in data:
    print(*x)