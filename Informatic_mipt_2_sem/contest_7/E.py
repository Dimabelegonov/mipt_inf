def main():
    data_1 = [[-1 for _ in range(8)] for _ in range(8)]
    data_2 = [[-1 for _ in range(8)] for _ in range(8)]
    a, b = map(lambda x: [ord(x[0]) - 97, int(x[1]) - 1], input().split())

    motions = [(1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]
    data_1[a[0]][a[1]] = 0
    data_2[b[0]][b[1]] = 0
    if a[0] == b[0] and a[1] == b[1]:
        return 0

    queue_1 = [(a[0], a[1])]
    queue_2 = [(b[0], b[1])]
    new_queue_1 = []
    new_queue_2 = []
    d = 1
    while len(queue_1) > 0 and d < 5:
        for x1, y1 in queue_1:
            for m in motions:
                if 0 <= x1 + m[0] < 8 and 0 <= y1 + m[1] < 8:
                    new_queue_1.append((x1 + m[0], y1 + m[1]))
                    data_1[x1 + m[0]][y1 + m[1]] = d

        # print(new_queue_1)

        for x2, y2 in queue_2:
            for m in motions:
                if 0 <= x2 + m[0] < 8 and 0 <= y2 + m[1] < 8:
                    new_queue_2.append((x2 + m[0], y2 + m[1]))
                    if data_1[x2 + m[0]][y2 + m[1]] == d:
                        return d
                    else:
                        data_2[x2 + m[0]][y2 + m[1]] = d

        queue_1 = list(new_queue_1)
        queue_2 = list(new_queue_2)
        new_queue_1 = []
        new_queue_2 = []
        d += 1

    return -1


print(main())
