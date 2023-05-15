c1, c2 = input().split()
if c1 == c2:
    print(0)
    quit()
x1, y1 = ord(c1[0]) - ord("a"), int(c1[1]) - 1
x2, y2 = ord(c2[0]) - ord("a"), int(c2[1]) - 1
table1 = [[-1 for _ in range(8)] for _ in range(8)]
table2 = [[-1 for _ in range(8)] for _ in range(8)]
table1[x1][y1] = 0
table2[x2][y2] = 0
possible_move = [[1, 2], [-1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, 1], [-2, -1]]
steps = 1
queue1 = [[x1, y1]]
queue2 = [[x2, y2]]

while len(queue1) * len(queue2) != 0 and steps < 5:
    new_queue1 = []
    new_queue2 = []
    for x, y in queue1:
        for nx, ny in possible_move:
            if -1 < x + nx < 7 and -1 < y + ny < 7:
                table1[x + nx][y + ny] = steps
                new_queue1.append([x + nx, y + ny])

    for x, y in queue2:
        for nx, ny in possible_move:
            if -1 < x + nx < 7 and -1 < y + ny < 7:
                if table1[x + nx][y + ny] == steps:
                    print(steps)
                    quit()
                table2[x + nx][y + ny] = steps
                new_queue2.append([x + nx, y + ny])

    queue1 = new_queue1.copy()
    queue2 = new_queue2.copy()
    steps += 1

print(-1)
quit()
