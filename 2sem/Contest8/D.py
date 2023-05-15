def make_table(N, M):
    table = []
    stack = []
    for i in range(N):
        a = list(map(int, input().split()))
        for j in range(M):
            if a[j] == 1:
                stack.append((i, j))
            else:
                a[j] = -1
        table.append(a)
    return stack, table


def table_operations(table, stack, N, M):
    distance = 0
    while len(stack) != 0:
        new_stack = []
        for x, y in stack:
            if table[x][y] > distance or table[x][y] == -1:
                table[x][y] = distance
                if x + 1 < N:
                    new_stack.append((x + 1, y))
                if x - 1 > -1:
                    new_stack.append((x - 1, y))
                if y + 1 < M:
                    new_stack.append((x, y + 1))
                if y - 1 > -1:
                    new_stack.append((x, y - 1))

        stack = new_stack.copy()
        distance += 1
    return table


N, M = map(int, input().split())
stack, table = make_table(N, M)
result = table_operations(table, stack, N, M)
for el in result:
    print(*el)
