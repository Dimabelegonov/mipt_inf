def bad_bridges(table, colours):
    cnt = 0
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == 0:
                continue
            elif colours[i] != colours[j]:
                cnt += 1
            table[i][j] = 0
            table[j][i] = 0
    return cnt


N = int(input())
table = [1] * N
for i in range(N):
    table[i] = list(map(int, input().split()))
empty_str = input()
colours = list(map(int, input().split()))

print(bad_bridges(table, colours))
