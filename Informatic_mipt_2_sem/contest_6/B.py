def main():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    data = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                data.append([i, j, matrix[i][j]])

    return data


for p in main():
    print(*p)


